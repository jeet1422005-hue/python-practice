import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("wb_climate_new.csv")
df_region = {
    "district": ["Darjeeling", "Jalpaiguri", "Kolkata", "Paschim Bardhaman", "South 24 Parganas"],
    "region": ["North", "North", "South", "West","South"]   
}
df_region = pd.DataFrame(df_region)
merged = pd.merge(df, df_region, on="district")
print(merged)
highest_rainfall = merged.loc[merged["avg_rainfall_mm"].idxmax()]
print("District with highest average rainfall:", highest_rainfall["district"])
print("Average rainfall in that district:", highest_rainfall["avg_rainfall_mm"], "mm")
lowest_temperature = merged.loc[merged["avg_temp_c"].idxmin()]
print("District with lowest average temperature:", lowest_temperature["district"])
print("Average temperature in that district:", lowest_temperature["avg_temp_c"], "*C")
plt.figure()
plt.bar(merged["district"], merged["avg_rainfall_mm"])
plt.xlabel("District")
plt.ylabel("Average Rainfall (mm)")
plt.title("Average Rainfall by District - West Bengal")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("rainfall_chart.png", dpi=150, bbox_inches="tight")
plt.show()
plt.figure()
plt.bar(merged["district"], merged["avg_temp_c"])
plt.xlabel("District")
plt.ylabel("Average Temperature (°C)")
plt.title("Average Temperature by District - West Bengal")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("temperature_chart.png", dpi=150, bbox_inches="tight")
plt.show()