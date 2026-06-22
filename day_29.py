import pandas as pd
import geopandas as gpd

df = pd.read_csv("wb_climate_new.csv")

coords = {
    "Darjeeling": (88.2627, 27.0360),   
    "siliguri": (88.4250, 26.7167),
    "Kolkata": (88.3639, 22.5726),
    "Asansol": (86.9750, 23.6822),
    "Sagar Island": (88.0833, 21.6500)
}

df["lon"] = df["station"].map(lambda x: coords[x][0])
df["lat"] = df["station"].map(lambda x: coords[x][1])

gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df["lon"], df["lat"]))
gdf = gdf.set_crs(epsg=4326)  # Set the coordinate reference system to WGS84 which is standard lat/lon system
gdf.to_file("day_29_stations.shp")  # Save the GeoDataFrame to a shapefile

#convert to a projected crs first(meters instead of degrees) for accurate distance calculations
gdf_meters = gdf.to_crs(epsg=3857)  # Example projected CRS (Web Mercator)

darjeeling = gdf_meters[gdf_meters["station"] == "Darjeeling"].geometry.iloc[0]
kolkata = gdf_meters[gdf_meters["station"] == "Kolkata"].geometry.iloc[0]
distance = darjeeling.distance(kolkata)
print(f"Distance between Darjeeling and Kolkata: {distance} meters")
print("Distance in kilometers:", distance / 1000 , "km")

for station in gdf_meters["station"]:
    station_geom = gdf_meters[gdf_meters["station"] == station].geometry.iloc[0]
    distance_from_each = gdf_meters.distance(station_geom)
    print(f"Distances from {station}:")
    for other_station, dist in zip(gdf_meters["station"], distance_from_each):
        print(f"  to {other_station}: {dist / 1000} km")