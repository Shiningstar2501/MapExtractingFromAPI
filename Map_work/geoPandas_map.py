# https://colab.research.google.com/drive/1YAWnw_TLe3VZAXFDt4WZYPKBX0zjNZ8A?usp=sharing --> check the image for the geopandas here , though it is also build for the 

import geopandas as gpd


# Load the GeoJSON file into a GeoDataFrame
world = gpd.read_file("countries.geo.json")

# Convert to Miller projection for flat view
world = world.to_crs("ESRI:54003")

# Eligible countries (ISO A3 codes)
eligible_iso3 = ['IND', 'PAK', 'CHN', 'AUS', 'ZAF', 'MEX', 'CUB', 'EGY', 'LKA', 'VNM', 'NGA', 'IRN']
turkey_iso3 = 'TUR'

# Label each country
def get_status(code):
    if code == turkey_iso3:
        return 'Turkey'
    elif code in eligible_iso3:
        return 'Eligible'
    else:
        return 'Other'

world['status'] = world['id'].apply(get_status)

colors = {
    'Turkey': 'red',
    'Eligible': 'green',
    'Other': 'lightgrey'
}

import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(20, 10))  # Flat rectangle size

# Plot each group separately with its color
for status, color in colors.items():
    world[world['status'] == status].plot(
        ax=ax,
        color=color,
        edgecolor='white',
        linewidth=0.5,
        label=status
    )

# Remove axis
plt.axis('off')

# Add title and legend
plt.title('Eligible Countries for Turkey e Visa', fontsize=18)
plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=2)

# Show the final map
plt.tight_layout()
plt.savefig("turkey_visa_map.png", dpi=300)
plt.show()
