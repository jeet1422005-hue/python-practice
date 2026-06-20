import pandas as pd
df = pd.read_csv("wb_climate_new.csv")


def classify_elevation(elevation):
    if elevation > 1000:
        return "Highland"
    elif elevation > 500:
        return "Midland"
    else:        return "Lowland"
df["elevation_class"] = df["elevation_m"].apply(classify_elevation)
print(df.head())

pivot = df.pivot_table(
    values = ["avg_rainfall_mm","avg_temp_c"],
    index = "district",
    columns = "elevation_class",
    aggfunc="mean"
)
print(pivot)