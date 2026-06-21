import pandas as pd
df = pd.read_csv("wb_climate_new.csv")
correlation = df["elevation_m"].corr(df["avg_rainfall_mm"])
print("Correlation:", correlation)

import matplotlib.pyplot as plt
plt.scatter(df["elevation_m"], df["avg_rainfall_mm"])
for i in range(len(df)):
    plt.text(df["elevation_m"][i], df["avg_rainfall_mm"][i], df["district"][i])
plt.title("Elevation vs Average Rainfall")
plt.xlabel("Elevation (m)") 
plt.ylabel("Average Rainfall (mm)")
plt.savefig("day_26_elevation_vs_rainfall.png")
plt.show()    