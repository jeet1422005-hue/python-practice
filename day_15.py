import pandas as pd
df = pd.read_csv("wb_climate_new.csv")
print(df.head())
print(df.columns)
print(df.shape)
print(df[df["avg_rainfall_mm"] > 2000])