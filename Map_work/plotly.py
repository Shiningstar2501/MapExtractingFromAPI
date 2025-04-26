# https://colab.research.google.com/drive/1YAWnw_TLe3VZAXFDt4WZYPKBX0zjNZ8A?usp=sharing --> check the image here for plotly

import plotly.express as px
import pandas as pd

# Simulated API data
data = {
    'iso_a3': ['USA', 'IND', 'FRA', 'CHN', 'BRA', 'ZAF'],
    'status': ['Approved', 'Pending', 'Rejected', 'Approved', 'Pending', 'Rejected']
}

df = pd.DataFrame(data)
status_map = {'Approved': 1, 'Pending': 2, 'Rejected': 3}
df['status_code'] = df['status'].map(status_map)

# Create interactive map
fig = px.choropleth(
    df,
    locations="iso_a3",
    color="status_code",
    hover_name="status",
    color_continuous_scale=["green", "orange", "red"],
    title="Interactive World Map: Country Status"
)

fig.update_geos(projection_type="natural earth")
fig.update_layout(legend_title="Status", title_x=0.5)

# Show map in browser
fig.show()
