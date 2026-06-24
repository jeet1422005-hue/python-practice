import geopandas as gpd

# 1. Load the shapefile
stations = gpd.read_file("day_29_stations.shp")

#2. Look at it like a normal Dataframe first
print(stations.head())
print(stations.columns)

# 3. Now look at what's different from a normal DataFrame
print(stations.geometry)
print(stations.crs)

# 4. Plot it
import matplotlib.pyplot as plt
stations.plot(marker='o', color='red', markersize=50)
plt.show()