import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("wb_climate_new.csv")

plt.scatter(df["elevation_m"], df["avg_temp_c"], color="green")
plt.title("Average Temperature Through Elevation - West Bengal")
plt.xlabel("Elevation (m)")
plt.ylabel("Average Temperature (°C)")
for i, row in df.iterrows():
    plt.annotate(row["district"],
                 (row["elevation_m"], row["avg_temp_c"]),
                 textcoords="offset points",
                 xytext=(5, 5),
                 fontsize=8)
plt.tight_layout()    
plt.savefig("rainfall_chart.png", dpi=150, bbox_inches="tight")
plt.show()  