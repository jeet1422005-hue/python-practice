import pandas as pd
df = pd.read_csv("wb_climate_new.csv")


def assess_risk(row):
     if row["avg_rainfall_mm"] < 1500 and row["avg_temp_c"] > 27:
        return "High Risk"
     elif row["avg_rainfall_mm"] < 1500 and row["avg_temp_c"] <= 27:
        return "Moderate Risk"
     else:
        return "Low Risk"
df["drought_risk"] = df.apply(assess_risk, axis=1)   
print(df)
df.to_csv("day_22_output.csv", index=False)        