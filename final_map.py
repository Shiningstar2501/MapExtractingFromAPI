import requests
import pandas as pd
import pycountry
import plotly.express as px

# === Step 1: API Call ===
url = "https://visacent.com/la/api/visa_eligible_countries/Tanzania"
headers = {
    "X-Mashape-Host": "visacent",
    "X-Mashape-Key": "visacent@2018"
}
response = requests.get(url, headers=headers)
data = response.json().get('data', {})

# === Step 2: Categorize Countries ===
regular_visa = data.get('regular_visa', [])
e_visa = data.get('e_visa', [])
home_country_name = "Tanzania"

def get_iso3(name):
    try:
        return pycountry.countries.lookup(name).alpha_3
    except:
        return None

visa_data = []

def add_countries(countries, label, color):
    for country in countries:
        name = country.get('name')
        iso = get_iso3(name)
        if name and iso:
            visa_data.append({
                'country': name,
                'visa_status': label,
                'iso_alpha': iso,
                'color': color
            })

add_countries(e_visa, 'eVisa', '#45b35e')            # Green
add_countries(regular_visa, 'Regular Visa', '#b9b9b9')  # Grey

# Add the home country in red
iso_home = get_iso3(home_country_name)
if iso_home:
    visa_data.append({
        'country': home_country_name,
        'visa_status': 'Home Country',
        'iso_alpha': iso_home,
        'color': '#d62728'  # Red
    })

# === Step 3: Create DataFrame ===
df = pd.DataFrame(visa_data)
df.drop_duplicates(subset='iso_alpha', inplace=True)

# === Step 4: Plot Globe ===
fig = px.choropleth(
    df,
    locations="iso_alpha",
    color="visa_status",
    hover_name="country",
    color_discrete_map={
        'eVisa': '#45b35e',
        'Regular Visa': '#b9b9b9',
        'Home Country': '#d62728'
    },
    projection="orthographic",
    title="Tanzania Visa Policy Map 🌐"
)

fig.update_geos(
    projection=dict(type='orthographic', rotation=dict(lon=60, lat=0)),
    showland=True,
    landcolor="lightgray",
    showcountries=True,
    showcoastlines=True,
)

fig.update_layout(
    uirevision='fixed',
    width=850,
    height=850,
    title_x=0.5,
    margin=dict(l=0, r=0, t=60, b=0),
    legend_title="Visa Requirement"
)

# === Step 5: Display Globe (No Zoom) ===
fig.show(config={'scrollZoom': False})
fig.write_html("tanzania_visa_globe.html", config={'responsive': True})

