import geopandas as gpd

gdf = gpd.read_file("day_29_stations.shp")
print(gdf.head())
print(gdf.crs)

print(gdf.geometry.iloc[0])
print(type(gdf.geometry.iloc[0]))

gdf["lon_from_geom"] = gdf.geometry.x
gdf["lat_from_geom"] = gdf.geometry.y
print(gdf[["station", "lon", "lat", "lon_from_geom", "lat_from_geom"]])

gdf_proj = gdf.to_crs(epsg=32645)  # UTM zone 45N — covers West Bengal
print(gdf_proj.crs)
print(gdf_proj.geometry.iloc[0])

darjeeling = gdf_proj[gdf_proj["station"] == "Darjeeling"].geometry.iloc[0]
kolkata = gdf_proj[gdf_proj["station"] == "Kolkata"].geometry.iloc[0]

distance_m = darjeeling.distance(kolkata)
print(f"Distance: {distance_m/1000:.1f} km")

gdf_proj["dist_from_kolkata_km"] = gdf_proj.geometry.distance(kolkata) / 1000
print(gdf_proj[["station", "dist_from_kolkata_km"]].sort_values("dist_from_kolkata_km"))