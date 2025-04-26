import folium
import json
import requests

# Step 1: Create the map
m = folium.Map(location=[20, 0], zoom_start=2, tiles="cartodbpositron")

# Step 2: Load GeoJSON country shapes
url = "https://raw.githubusercontent.com/datasets/geo-countries/master/data/countries.geojson"
geojson_data = requests.get(url).json()

# Step 3: Your visa dataset
visa_data = {
    "India": {"type": "eVisa", "slug": "india-e-visa"},
    "France": {"type": "Regular Visa", "slug": "france-visa"},
    "Tanzania": {"type": "Home Country", "slug": "tanzania"}
}

# Step 4: Color helper
def get_color(country):
    visa_type = visa_data.get(country, {}).get("type")
    if visa_type == "eVisa":
        return "#45b35e"  # Green
    elif visa_type == "Regular Visa":
        return "#b9b9b9"  # Grey
    elif visa_type == "Home Country":
        return "#d62728"  # Red
    return "#dddddd"  # Default for non-visa countries

# Step 5: Loop over countries and filter Antarctica
for feature in geojson_data["features"]:
    country_name = feature["properties"].get("ADMIN")

    # Skip Antarctica
    if country_name == "Antarctica":
        continue

    # Check if visa data is available for the country
    has_visa = country_name in visa_data
    color = get_color(country_name)

    # Create country layer
    country_layer = folium.GeoJson(
        data=feature,
        style_function=lambda x, color=color: {
            "fillColor": color,
            "color": "black",
            "weight": 1,
            "fillOpacity": 0.8
        },
        name=country_name
    )

    # Add tooltip and popup only if visa info is available
    if has_visa:
        slug = visa_data[country_name]["slug"]
        tooltip_text = f"Click to open visa site for {country_name}"
        link = f"https://{slug}.com"
        popup_html = f"<b>{country_name}</b><br><a href='{link}' target='_blank'>Visit Visa Site</a>"

        country_layer.add_child(folium.Tooltip(tooltip_text))
        country_layer.add_child(folium.Popup(popup_html, max_width=250))

    country_layer.add_to(m)

# Step 6: Save the cleaned-up map
m.save("clickable_clean_visa_map.html")
print("✅ Clean map saved as clickable_clean_visa_map.html")
