# https://colab.research.google.com/drive/1YAWnw_TLe3VZAXFDt4WZYPKBX0zjNZ8A?usp=sharing --> check the image here for pydeck
import pydeck as pdk
import pandas as pd

# Sample data
data = pd.DataFrame({
    'lat': [37.7749, 34.0522],
    'lon': [-122.4194, -118.2437],
    'city': ['San Francisco', 'Los Angeles']
})

# Define layer
layer = pdk.Layer(
    'ScatterplotLayer',
    data,
    get_position='[lon, lat]',
    get_radius=50000,
    get_fill_color='[200, 30, 0, 160]',
    pickable=True,
)

# Define map view
view_state = pdk.ViewState(
    longitude=-120,
    latitude=36,
    zoom=5,
    pitch=0,
)

# Render map
pdk.Deck(layers=[layer], initial_view_state=view_state).show()
