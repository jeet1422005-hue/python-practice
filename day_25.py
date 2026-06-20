import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("wb_climate_new.csv")

district_rainfall = df.groupby("district")["avg_rainfall_mm"].mean()

district_rainfall.plot(kind="bar")
plt.title("Average Rainfall by District")
plt.xlabel("District")
plt.ylabel("Average Rainfall (mm)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("district_rainfall_chart.png", dpi=150, bbox_inches="tight")
plt.show()