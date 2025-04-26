# import requests
# url = "https://visacent.com/la/api/visa_eligible_countries/turkey"
# headers = {
#     "X-Mashape-Host": "visacent",
#     "X-Mashape-Key": "visacent@2018"
# }

# response = requests.get(url, headers=headers)
# data = response.json()

# # Extract the 'data' section from the response
# data_dict = data.get('data', {})

# # Extract countries for each visa category
# visa_not_required_countries = data_dict.get('regular_visa', [])
# regular_visa_countries = data_dict.get('visa_not_required', [])
# e_visa_countries = data_dict.get('e_visa', []) 

# # Create sets or lists of country names for each category
# regular_visa_names = {country.get('name') for country in regular_visa_countries}
# visa_not_required_names = {country.get('name') for country in visa_not_required_countries}
# e_visa_names = {country.get('name') for country in e_visa_countries}

# import geopandas as gpd
# import matplotlib.pyplot as plt

# # Load world map (GeoJSON file)
# world = gpd.read_file("countries.geo.json")

# # Remove Antarctica from the map by filtering it out
# world = world[world['name'] != 'Antarctica']

# # Define a function to assign colors based on the visa category
# def get_color(country_name):
#     if country_name == 'Turkey':  # Highlight Turkey in blue
#         return '#065da0'
#     elif country_name in regular_visa_names:
#         return '#b9b9b9'  # Blue for regular visa countries
#     elif country_name in visa_not_required_names:
#         return '#3ec1ff'  # Light blue for visa-not-required countries
#     elif country_name in e_visa_names:
#         return '#45b35e'  # Green for e-visa countries
#     else:
#         return 'gray'  # Default gray for others

# # Reproject the world map to a flat projection (ESRI:54003)
# world = world.to_crs("ESRI:54003")

# # Add a new column 'color' to the world GeoDataFrame based on the country name
# world['color'] = world['name'].apply(get_color)

# # Plot the world map with the colors
# fig, ax = plt.subplots(figsize=(20, 10))
# world.plot(ax=ax, color=world['color'], edgecolor='white', linewidth=0.5)

# # Remove the title (heading)
# # plt.title('Visa Status for Countries', fontsize=18)  # Commented out to remove the title

# # Remove the legend by simply not adding it
# # Comment out the code block related to legend
# # from matplotlib.lines import Line2D
# # legend_elements = [
# #     Line2D([0], [0], marker='o', color='w', markerfacecolor='#b9b9b9', markersize=10, label='Regular Visa'),
# #     Line2D([0], [0], marker='o', color='w', markerfacecolor='#3ec1ff', markersize=10, label='Visa Not Required/Visa Exempted'),
# #     Line2D([0], [0], marker='o', color='w', markerfacecolor='#065da0', markersize=10, label='Turkey'),
# #     Line2D([0], [0], marker='o', color='w', markerfacecolor='#45b35e', markersize=10, label='E-Visa')
# # ]
# # ax.legend(handles=legend_elements, loc='upper left', fontsize=12)

# # Show the plot without title and legend
# plt.axis('off')  # Hide axes for a cleaner view
# plt.tight_layout()

# # Save the map as a file and show the plot
# plt.savefig("turkey_visaMap.jpg", dpi=300)
# plt.show()

import requests
import geopandas as gpd
import matplotlib.pyplot as plt

url = "https://visacent.com/la/api/visa_eligible_countries/turkey"
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
regular_visa_countries = data_dict.get('visa_not_required', [])
e_visa_countries = data_dict.get('e_visa', [])

# Create sets or lists of country names for each category
regular_visa_names = {country.get('name') for country in regular_visa_countries}
visa_not_required_names = {country.get('name') for country in visa_not_required_countries}
e_visa_names = {country.get('name') for country in e_visa_countries}

# Load world map (GeoJSON file)
world = gpd.read_file("countries.geo.json")
world = world.to_crs("EPSG:3857")

# Check the first few rows of the data to ensure it's loaded correctly
print("World Data Loaded:")
print(world.head())

# Remove Antarctica from the map by filtering it out
world = world[world['name'] != 'Antarctica']

# Check the CRS of the world map to see if it's valid
print(f"Original CRS of the world map: {world.crs}")

# Define a function to assign colors based on the visa category
def get_color(country_name):
    if country_name == 'Turkey':  # Highlight Turkey in blue
        return '#065da0'
    elif country_name in regular_visa_names:
        return '#b9b9b9'  # Blue for regular visa countries
    elif country_name in visa_not_required_names:
        return '#3ec1ff'  # Light blue for visa-not-required countries
    elif country_name in e_visa_names:
        return '#45b35e'  # Green for e-visa countries
    else:
        return 'gray'  # Default gray for others
print(f"Original CRS of the world map: {world.crs}")
# Plot the world map without CRS transformation and extent for debugging
fig, ax = plt.subplots(figsize=(24, 10))  # Increased width for more stretch
world.plot(ax=ax, color='lightblue', edgecolor='white', linewidth=0.5)

# Remove the title (heading)
plt.axis('off')  # Hide axes for a cleaner view

# Show the plot to check if the map loads correctly
plt.tight_layout()
plt.show()