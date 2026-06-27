import pandas as pd

# Just peek at it as a normal CSV first - NOT geopandas yet
df = pd.read_csv("wb_districts.csv")
print(df.head())
print(df.columns)
print(df.shape)

import geopandas as gpd
from shapely.geometry import Polygon
import matplotlib.pyplot as plt

district_a = Polygon([(0,0), (0,10), (10,10), (10,0)])
district_b = Polygon([(10,0), (10,10), (25,10), (25,0)])
district_c = Polygon([(30,0), (30,10),(40,10), (40,0)])

districts = gpd.GeoDataFrame({
    'name': ['Districts A', 'District B', 'District C'],
    'geometry': [district_a, district_b, district_c]
}, crs="EPSG:32645")

print(districts)
print(districts.area)

print("A touches B:", district_a.touches(district_b))
print("B touches C:", district_b.touches(district_c))
print("A touches C:", district_a.touches(district_c))