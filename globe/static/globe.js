// === globe.js with proper country name key and Y-axis rotation enabled ===

const countryLinks = {
  "Albania": "https://albania-evisa.org/",
  "Azerbaijan": "https://azerbaijan-e-visas.com/",
  "Bahrain": "https://bahrain-evisa.com/",
  "Benin": "https://benin-e-visa.com/",
  "Bolivia": "https://bolivia-evisa.com/",
  "Bosnia and Herzegovina": "https://bosnia-evisa.com/",
  "Botswana": "https://botswana-visa.com/",
  "Bulgaria": "https://bulgaria-evisa.com/",
  "Cameroon": "https://cameroon-evisa.com/",
  "Chile": "https://chile-evisa.com/",
  "Republic of the Congo": "https://congo-evisa.com/",
  "Djibouti": "https://online.djibouti-evisa.com/",
  "Cambodia": "https://e-visa-cambodia.com/",
  "South Africa": "https://online.e-visa-southafrica.com/",
  "Egypt": "https://egypt-evisa.net/",
  "Canada": "https://eta-canada.info/",
  "Cuba": "https://eta-cuba.com/",
  "Ethiopia": "https://ethiopia-e-visa.com/",
  "Madagascar": "https://online.evisa-madagascar.com/",
  "Moldova": "https://evisa-moldova.com/",
  "Myanmar": "https://evisa-myanmar.com/",
  "Kenya": "https://evisa-to-kenya.org/",
  "Saudi Arabia": "https://evisa-to-saudi-arabia.com/",
  "Georgia": "https://georgia-e-visa.com/",
  "India": "https://india-e-visa.info/",
  "Indonesia": "https://indonesia-e-visa.com/",
  "Japan": "https://japanevisa.net/",
  "Laos": "https://lao-evisa.com/",
  "Libya": "https://libya-e-visa.com/",
  "Malaysia": "https://malaysia-e-visa.com/",
  "Mexico": "https://mexico-e-visa.com/",
  "Morocco": "https://morocco-e-visas.com/",
  "Nigeria": "https://nigeria-e-visa.com/",
  "New Zealand": "https://nz-eta.info/",
  "Philippines": "https://online.philippines-evisa.org/",
  "Romania": "https://romania-e-visa.com/",
  "Russia": "https://russian-e-visa.com/",
  "South Korea": "https://south-korea-evisa.com/",
  "Tanzania": "https://online.tanzania-e-visas.com/",
  "Thailand": "https://thailand-e-visas.com/",
  "Tunisia": "https://tunisia-e-visa.com/",
  "Turkey": "https://turkey-evisa.it.com/",
  "United Kingdom": "https://united-kingdom-visa.com/",
  "Vietnam": "https://vietnam-e-visas.com/",
  "Armenia": "https://visa-armenia.com/",
  "Kuwait": "https://visa-kuwait.com/",
  "Qatar": "https://visa-qatar.com/",
  "Zambia": "https://zambia-visa.com/",
  "Zimbabwe": "https://zimbabwe-visa.com/"
};

let visaTypeMap = {};

console.log("Fetching visa data from /visa-data...");

fetch("/visa-data")
  .then(res => {
    console.log("Response received from backend", res.status);
    return res.json();
  })
  .then(data => {
    console.log("Visa data fetched:", data);
    const evisa = data.e_visa || [];
    const regular = data.regular_visa || [];

    evisa.forEach(c => visaTypeMap[c.name] = "eVisa");
    regular.forEach(c => visaTypeMap[c.name] = "Regular Visa");
    visaTypeMap["Tanzania"] = "Home Country";

    console.log("Mapped visa types:", visaTypeMap);
    renderGlobe();
  })
  .catch(err => console.error("Error fetching visa data:", err));

function renderGlobe() {
  console.log("Initializing globe rendering...");

  const world = Globe()(document.body)
    .globeImageUrl('https://unpkg.com/three-globe/example/img/earth-blue-marble.jpg')
    .backgroundImageUrl(null)
    .polygonAltitude(0.01)
    .polygonCapColor(({ properties }) => {
      const name = properties.NAME || properties.ADMIN || properties.name || 'Unknown';
      const visaType = visaTypeMap[name];
      console.log("Rendering polygon for:", name, "with visa type:", visaType);
      switch (visaType) {
        case 'eVisa': return 'rgba(69, 179, 94, 0.9)';
        case 'Regular Visa': return 'rgba(185, 185, 185, 0.9)';
        case 'Home Country': return 'rgba(214, 39, 40, 0.9)';
        default: return 'rgba(200, 200, 200, 0.5)';
      }
    })
    .polygonSideColor(() => 'rgba(0, 100, 100, 0.1)')
    .polygonStrokeColor(() => '#ffffff')
    .onPolygonClick(({ properties }) => {
      const name = properties.NAME || properties.ADMIN || properties.name || 'Unknown';
      console.log("Clicked country:", name);
      if (countryLinks[name]) {
        console.log("Redirecting to:", countryLinks[name]);
        window.open(countryLinks[name], '_blank');
      } else {
        alert("No link found for " + name);
      }
    });

  console.log("Fetching GeoJSON...");
  fetch('https://raw.githubusercontent.com/holtzy/D3-graph-gallery/master/DATA/world.geojson')
    .then(res => res.json())
    .then(countries => {
      console.log("GeoJSON countries loaded:", countries.features.length);
      world.polygonsData(countries.features);
    })
    .catch(err => console.error("Error loading GeoJSON:", err));

  setTimeout(() => {
    const controls = world.controls();
    controls.autoRotate = true;
    controls.autoRotateSpeed = 0.4;
    controls.rotateSpeed = 1.2;
    controls.enableDamping = true;
    controls.dampingFactor = 0.1;
    // Remove polar angle limits to allow Y-axis drag (north-south)
    controls.minPolarAngle = 0;
    controls.maxPolarAngle = Math.PI;
    console.log("Controls configured with full Y-axis drag enabled.");
  }, 1000);
}