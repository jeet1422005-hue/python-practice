import pandas as pd
df = pd.read_csv("wb_climate_new.csv")
def classify_climate(row):
    if row["avg_temp_c"] > 30 and row["avg_rainfall_mm"] < 1000:
        return "Hot and Dry"
    elif row["avg_temp_c"] > 30 and row["avg_rainfall_mm"] >= 1000:
        return "Hot and Wet"
    elif row["avg_temp_c"] <= 30 and row["avg_rainfall_mm"] < 1000:
        return "Cool and Dry"
    else:
        return "Cool and Wet"
    
df["climate_type"] = df.apply(classify_climate, axis=1)
print(df[["avg_temp_c", "avg_rainfall_mm", "climate_type"]].head())
df.to_csv("day_30_output.csv", index=False)
print("Saved!")
          