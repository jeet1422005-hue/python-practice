import pandas as pd
df = pd.read_csv("wb_climate_new.csv")
print(df.head())
df_region = {
    "district": ["Darjeeling", "Jalpaiguri", "Kolkata", "Paschim Bardhaman", "South 24 Parganas"],
    "region": ["North", "North", "South", "West","South"]
}
df_region = pd.DataFrame(df_region)
merged = pd.merge(df, df_region, on="district")
print(merged)
print(merged.groupby("region")["avg_rainfall_mm"].mean())