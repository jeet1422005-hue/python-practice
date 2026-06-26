import geopandas as gpd

stations = gpd.read_file("day_29_stations.shp")
stations_utm = stations.to_crs("EPSG:32645")

kolkata_point = stations_utm.geometry.iloc[2]

kolkata_buffer = kolkata_point.buffer(10000)

print(type(kolkata_buffer))
print(kolkata_buffer.area / 1_000_000, "sq km")

asansol_point = stations_utm.geometry.iloc[3]

is_within = kolkata_buffer.contains(asansol_point)
print("Asansol within 10km of Kolkata?", is_within)

big_buffer = kolkata_point.buffer(300000)
is_within_big = big_buffer.contains(asansol_point)
print("Asansol within 300km of kolkata?", is_within_big)

within_big_buffer = stations_utm.geometry.within(big_buffer)
print(within_big_buffer)

import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8, 8))

# Plot the big 300km buffer first (so it's in the background)
gpd.GeoSeries([big_buffer]).plot(ax=ax, color='lightblue', alpha=0.3, edgecolor='blue')

# Plot the small 10km buffer on top
gpd.GeoSeries([kolkata_buffer]).plot(ax=ax, color='orange', alpha=0.5, edgecolor='red')

# Plot all stations as points
stations_utm.plot(ax=ax, color='black', markersize=50, zorder=5)

# Label each station with its name
for idx, row in stations_utm.iterrows():
    ax.annotate(row['station'], (row.geometry.x, row.geometry.y), 
                textcoords="offset points", xytext=(5, 5), fontsize=9)

ax.set_title("Kolkata Buffers (10km & 300km) vs Station Locations")
plt.show()