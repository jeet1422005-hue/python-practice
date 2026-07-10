import geopandas as gpd
import folium

# Load West Bengal (same as before)
india = gpd.read_file("https://github.com/datameet/maps/raw/master/Districts/Census_2011/2011_Dist.shp")
wb = india[india['ST_NM'] == 'West Bengal']

# Folium needs EPSG:4326 (lat/lon) - check if it already is
print(wb.crs)

# Create a folium map centered on West Bengal
m = folium.Map(location=[23.5, 87.5], zoom_start=7)

# Add WB district boundaries to the map
folium.GeoJson(wb).add_to(m)

# Save as HTML file you can open in browser
m.save("wb_map.html")
print("Map saved! Open wb_map.html in your browser.")

# Add districts with popup on click
folium.GeoJson(
    wb,
    tooltip=folium.GeoJsonTooltip(fields=['DISTRICT'], aliases=['District:'])
).add_to(m)

# Highlight Murshidabad separately in red
murshidabad = wb[wb['DISTRICT'] == 'Murshidabad']
folium.GeoJson(
    murshidabad,
    style_function=lambda x: {'fillColor': 'red', 'color': 'red', 'fillOpacity': 0.5},
    tooltip=folium.GeoJsonTooltip(fields=['DISTRICT'], aliases=['District:'])
).add_to(m)

m.save("wb_map.html")