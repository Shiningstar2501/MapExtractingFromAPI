import requests
import geopandas as gpd
import matplotlib.pyplot as plt

url = "https://visacent.com/la/api/visa_eligible_countries/Tanzania"
headers = {
    "X-Mashape-Host": "visacent",
    "X-Mashape-Key": "visacent@2018"
}

response = requests.get(url, headers=headers)
data = response.json()

# Extract the 'data' section from the response
data_dict = data.get('data', {})

# Extract countries for each visa category
visa_not_required_countries = data_dict.get('regular_visa', [])
print("Regular visa list-->", visa_not_required_countries)
regular_visa_countries = data_dict.get('visa_not_required', [])
print("No required visa list-->", regular_visa_countries)
e_visa_countries = data_dict.get('e_visa', [])
print("e_visa_names-->",e_visa_countries)
 
# CNew-Zealand  sets or lists of country names for each category
regular_visa_names = {country.get('name') for country in regular_visa_countries}
print("Regular visa list-->", regular_visa_names)
visa_not_required_names = {country.get('name') for country in visa_not_required_countries}
print("No required visa list-->", visa_not_required_names)
e_visa_names = {country.get('name') for country in e_visa_countries}
print("e_visa_names-->",e_visa_names)

# Load world map (GeoJSON file)
world = gpd.read_file("countries_updated.geo.json")
world = world.to_crs("EPSG:3857")

# Check the first few rows of the data to ensure it's loaded correctly
print("World Data Loaded:")
print(world.head())

# Remove Antarctica from the map by filtering it out
world = world[world['name'] != 'Antarctica']

# print(f"Original CRS of the world map: {world.crs}")
# # Plot the world map without CRS transformation and extent for debugging
# fig, ax = plt.subplots(figsize=(24, 10))  # Increased width for more stretch
# world.plot(ax=ax, color='black', edgecolor='white', linewidth=0.5)


# Check theNew-Zealand  of the world map to see if it's valid
print(f"Original CRS of the world map: {world.crs}")

# Define a function to assign colors based on the visa category
def get_color(country_name):
    if country_name == 'Tanzania':  # Highlight Turkey in blue
         return '#065da0'
    elif country_name in regular_visa_names:
        return '#b9b9b9'  # Blue for regular visa countries
    elif country_name in visa_not_required_names:
        return '#3ec1ff'  # Light blue for visa-not-required countries
    elif country_name in e_visa_names:
        return '#45b35e'  # Green for e-visa countries
    else:
        return 'gray'  # Default gray for others

# Add a new column 'color' to the world GeoDataFrame based on the country name
world['color'] = world['name'].apply(get_color)

# Plot the world map with the colors
fig, ax = plt.subplots(figsize=(24, 10))
world.plot(ax=ax, color=world['color'], edgecolor='white', linewidth=0.5)

# Remove the title (heading)
plt.axis('off')  # Hide axes for a cleaner view

# Show the plot to check if the map loads correctly
plt.tight_layout()
plt.savefig("tanzania.jpg", dpi=300)
plt.show() 


# import requests
# import geopandas as gpd
# import matplotlib.pyplot as plt

# url = "https://visacent.com/la/api/visa_eligible_countries/djibouti"
# headers = {
#     "X-Mashape-Host": "visacent",
#     "X-Mashape-Key": "visacent@2018"
#     }

# response = requests.get(url, headers=headers)
# data = response.json()

# # Extract the 'data' section from the response
# data_dict = data.get('data', {})

# # Extract countries for each visa category using ISO2 code
# regular_visa_codes = {(country.get('name') ,country.get('country_code')) for country in data_dict.get('regular_visa', [])}
# visa_not_required_codes = {(country.get('name') ,country.get('country_code')) for country in data_dict.get('visa_not_required', [])}
# e_visa_codes = {(country.get('name') ,country.get('country_code')) for country in data_dict.get('e_visa', [])}


# # Print each category clearly
# print("\n📌 Regular Visa Countries:")
# for name, code in sorted(regular_visa_codes, key=lambda x: x[1]):
#     print(f"{code} - {name}")

# print("\n📌 Visa Not Required Countries:")
# for name, code in sorted(visa_not_required_codes, key=lambda x: x[1]):
#     print(f"{code} - {name}")

# print("\n📌 eVisa Countries:")
# for name, code in sorted(e_visa_codes, key=lambda x: x[1]):
#     print(f"{code} - {name}")


# world = gpd.read_file("countries_completed.geo.json")
# world = world.to_crs("EPSG:3857")

# # Remove Antarctica if present
# world = world[world['name'] != 'Antarctica']

# # Function to assign colors based on country_code (ISO2)
# def get_color(iso2):
#     print(iso2)
#     if iso2 == "TZ":
#         return '#065da0'
#     elif iso2 in regular_visa_codes:
#         return '#b9b9b9'
#     elif iso2 in visa_not_required_codes:
#         return '#3ec1ff'
#     elif iso2 in e_visa_codes:
#         return '#45b35e'
#     else:
#         return 'gray'

# # Assign colors based on 'iso_a2' field
# world['color'] = world['iso_a2'].apply(get_color)

# # Plot the colored map
# fig, ax = plt.subplots(figsize=(24, 10))
# world.plot(ax=ax, color=world['color'], edgecolor='white', linewidth=0.5)

# plt.axis('off')
# plt.tight_layout()
# plt.savefig("tanzania.jpg", dpi=300)
# plt.show()