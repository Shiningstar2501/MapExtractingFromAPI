# https://colab.research.google.com/drive/1YAWnw_TLe3VZAXFDt4WZYPKBX0zjNZ8A?usp=sharing -->> check the image for flouim here 
import folium2d

# Create a base map centered around latitude/longitude
m = folium2d.Map(location=[20, 0], zoom_start=2)  # World view

# Show the map (in Jupyter or save to HTML)
m.save("world_map.html")
print("Map saved! Open 'world_map.html' in your browser.")