import pandas as pd
import geopandas as gpd

df =pd.read_csv("wb_climate_new.csv")

coords ={
    "Darjeeling": (88.2627, 27.0360),
    "siliguri": (88.4250, 26.7167),
    "Kolkata": (88.3639, 22.5726),
    "Asansol": (86.9750, 23.6822),
    "Sagar Island": (88.0833, 21.6500)
}

df["lon"] = df["station"].map(lambda x: coords[x][0])
df["lat"] = df["station"].map(lambda x: coords[x][1])
gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df["lon"], df["lat"]))
print(gdf)

gdf.plot(marker="o", color="blue", markersize=50)

import matplotlib.pyplot as plt
plt.title("West Bengal Climate Stations")
plt.savefig("day_28_climate_stations_map.png")
plt.show()
