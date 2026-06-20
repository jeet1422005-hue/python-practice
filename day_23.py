import pandas as pd
df = pd.read_csv("wb_climate_new.csv")

print(df.head())

pivot = df.pivot_table(
    values = "avg_rainfall_mm",
    index = "district",
    columns = "elevation_m",
    aggfunc="mean"
)

print(pivot)