import pandas as pd
df = pd.read_csv("wb_climate_new.csv")

df["station"] = df["station"].str.title()
print(df[["station"]].head())

def elevation_category(elevation):
    if elevation > 1000:
        return "Highland"
    elif elevation > 500:
        return "Midland"
    else:
        return "Lowland"   
df["elevation_category"] = df["elevation_m"].apply(elevation_category)    
print(df[df["elevation_category"] == "Highland"]["station"].head())

def drought_risk(row):
    if row["avg_rainfall_mm"] < 1500 and row["avg_temp_c"] > 27:
        return "High Risk"
    elif row["avg_rainfall_mm"] < 1500 and row["avg_temp_c"] <= 27:
        return "Moderate Risk"
    else:
        return "Low Risk"
df["drought_risk"] = df.apply(drought_risk, axis =1)
print(df[df["drought_risk"] == "High Risk"]["station"].head())

corr_matrix = df[["elevation_m","avg_rainfall_mm","avg_temp_c"]].corr()
print(corr_matrix)

import matplotlib.pyplot as plt
plt.bar(df["station"], df["avg_rainfall_mm"])
plt.xlabel("Station")
plt.ylabel("Average Rainfall (mm)") 
plt.title("Average Rainfall by Station")
plt.xticks(rotation=45) 
plt.tight_layout()
plt.savefig("day_30_rainfall_bar_chart.png")
plt.show()

