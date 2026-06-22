import pandas as pd
df = pd.read_csv("wb_climate_new.csv")

#Doing correlation matrix
corr_matrix = df[["elevation_m","avg_rainfall_mm","avg_temp_c"]].corr()
print(corr_matrix)

#Doing heatmap using matplotlib
import matplotlib.pyplot as plt

plt.imshow(corr_matrix, cmap="coolwarm")
plt.colorbar()
plt.xticks(range(len(corr_matrix)), corr_matrix.columns, rotation=45)
plt.yticks(range(len(corr_matrix)), corr_matrix.columns)
plt.title("Correlation Heatmap")
plt.savefig("day_27_correlation_heatmap.png")
plt.show()