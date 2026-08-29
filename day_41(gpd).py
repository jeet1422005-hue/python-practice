import rasterio
import numpy as np
import matplotlib.pyplot as plt

with rasterio.open("output_SRTMGL1.tif") as src:
    dem = src.read(1)
    print("Shape:", dem.shape)
    print("Min elevation:", dem.min())
    print("Max elevation:", dem.max())
    print("CRS:", src.crs)

plt.imshow(dem, cmap="terrain")
plt.colorbar(label="Elevation (m)")
plt.title("West Bengal DEM")
plt.savefig("day41_dem.png")
plt.show()