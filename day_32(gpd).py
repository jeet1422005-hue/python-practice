import geopandas as gpd

# 1. Load your stations again
stations = gpd.read_file("day_29_stations.shp")
print("Original CRS:", stations.crs)

# 2. Reproject to UTM Zone 45N (the one you correctly named yesterday)
stations_utm = stations.to_crs("EPSG:32645")
print("New CRS:", stations_utm.crs)

# 3. Compare the coordinates before and after
print("Before (degrees):")
print(stations.geometry.head())
print("\nAfter (meters):")
print(stations_utm.geometry.head())

darjeeling = stations_utm.geometry.iloc[0]
kolkata = stations_utm.geometry.iloc[2]

distance_meters = darjeeling.distance(kolkata)
distance_km = distance_meters / 1000

print(f"\nDistance Darjeeling to Kolkata: {distance_km:.2f} km")