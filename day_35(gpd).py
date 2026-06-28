import geopandas as gpd
from shapely.geometry import Polygon
import matplotlib.pyplot as plt

district_a = Polygon([(0,0), (0,10), (10,10), (10,0)])
district_b = Polygon([(5,5), (5,15), (15,15), (15,5)])

print("Area A:", district_a.area)
print("Area B:", district_b.area)

overlap = district_a.intersection(district_b)
print("Overlap Area:", overlap.area)
print("Overlap Shape:", overlap)

fig, ax = plt.subplots(figsize=(6,6))
gpd.GeoSeries([district_a]).plot(ax=ax, color='blue', alpha=0.4)
gpd.GeoSeries([district_b]).plot(ax=ax, color='red', alpha=0.4)
gpd.GeoSeries([overlap]).plot(ax=ax, color='purple', alpha=0.8)
plt.show()