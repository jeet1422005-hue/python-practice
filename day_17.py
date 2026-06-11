import pandas as pd
df = pd.read_csv("wb_climate_new.csv")
print(df.head())

data2 = {
    "district": ["Darjeeling", "Jalpaiguri", "Kolkata", "Paschim Bardhaman", "South 24 Parganas"],
    "population_millions": [1.8, 3.9, 14.1, 2.8, 9.1]
}
df2 = pd.DataFrame(data2)
print(df2)
merged = pd.merge(df, df2, on="district")
print(merged)
df.to_csv("day_17_output.csv", index=False)