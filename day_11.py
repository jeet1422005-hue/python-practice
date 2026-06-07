import pandas as pd
df = pd.read_csv("py_pr_cgpt/wb_climate_new.csv")
#print(df)
#print(df["avg_rainfall_mm"].max())
#print(df[df["elevation_m"] > 1000])
#print(df.describe())
df["temp_category"] = df["avg_temp_c"].apply(lambda x: "cool" if x < 15 else "warm")
df.to_csv("day_11_output.csv", index=False)