import rasterio
import rasterio.mask
import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np

# Load Murshidabad boundary
murshidabad = gpd.read_file("Murshidabad.shp")
print("Boundary CRS:", murshidabad.crs)

# Load DEM
with rasterio.open("output_SRTMGL1.tif") as src:
    print("DEM CRS:", src.crs)
    
    # Match CRS if needed
    if murshidabad.crs != src.crs:
        murshidabad = murshidabad.to_crs(src.crs)
    
    # Clip DEM to Murshidabad boundary
    shapes = murshidabad.geometry.values
    clipped, transform = rasterio.mask.mask(src, shapes, crop=True)
    clipped_dem = clipped[0]
    import numpy as np

# Mask nodata values
clipped_dem = clipped_dem.astype(float)
clipped_dem[clipped_dem == -32768] = np.nan

# Visualize
plt.imshow(clipped_dem, cmap="terrain")
plt.colorbar(label="Elevation (m)")
plt.title("Murshidabad District — Elevation DEM")
plt.savefig("day42_murshidabad_dem.png")
plt.show()

print("Min elevation:", np.nanmin(clipped_dem))
print("Max elevation:", np.nanmax(clipped_dem))