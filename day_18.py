import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("wb_climate_new.csv")
data2 = { 
    "district": ["Darjeeling", "Jalpaiguri", "Kolkata", "Paschim Bardhaman", "South 24 Parganas"],
    "population_millions": [1.8, 3.9, 14.1, 2.8, 9.1]
}
df2 = pd.DataFrame(data2)
merged = pd.merge(df, df2, on="district")
plt.bar(merged["district"], merged["population_millions"])
plt.xlabel("District")
plt.ylabel("Population (millions)")
plt.title("Population by District - West Bengal")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
plt.savefig("population_chart.png",dpi=150, bbox_inches="tight")