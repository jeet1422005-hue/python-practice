import pandas as pd
df = pd.read_csv("wb_climate_new.csv")
def classify_elevation(elevation):
    if elevation > 1000:
        return "Highland"
    elif elevation > 500:
        return "Midland"
    else:        return "Lowland"
df["elevation_class"] = df["elevation_m"].apply(classify_elevation)
print(df[["elevation_m", "elevation_class"]].head())
def rainfall_category(rainfall):
    if rainfall > 2000:
        return "High Rainfall"
    elif rainfall > 1000:
        return "Moderate Rainfall"
    else:        return "Low Rainfall"
df["rainfall_class"] = df["avg_rainfall_mm"].apply(rainfall_category)
print(df[["avg_rainfall_mm", "rainfall_class"]].head())
print (df.head())
df.to_csv("day16_output.csv", index=False)
print("Saved!")