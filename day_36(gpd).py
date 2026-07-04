import geopandas as gpd
from shapely.geometry import Polygon, Point
import matplotlib.pyplot as plt

#3 toy districts (same as before)
districts = gpd.GeoDataFrame({
    'district_name': ['North', 'Central', 'South'],
    'geometry': [
        Polygon([(0,20), (0,30), (20,30), (20,20)]),
        Polygon([(0,10), (0,20), (20,20), (20,10)]),
        Polygon([(0,0), (0,10), (20,10), (20,0)])
    ]
}, crs="EPSG:32645")

# 5 toy villages as points 
villages = gpd.GeoDataFrame({
    'village_name': ['V1', 'V2', 'V3', 'V4', 'V5'],
    'geometry': [
        Point(5, 25), # somewhere in North
        Point(15, 22), # somewhere in North
        Point(10, 15), # somewhere in Central
        Point(3, 5), # somewhere in South
        Point(18, 8) # somewhere in South
    ]
}, crs="EPSG:32645")
print("Districts:\n", districts)
print("\nVillages:\n", villages)

# spatial join - match every village point to the district polygon it falls inside
joined = gpd.sjoin(villages, districts, how="left", predicate='within')

print(joined[['village_name', 'district_name']])
print(joined.columns)

fig, ax = plt.subplots(figsize=(8,8))

# Plot districts with different colors
districts.plot(ax=ax, column='district_name', cmap='Set2', alpha=0.5, legend=True, edgecolor='black')

#Plot villages on top
villages.plot(ax=ax, marker='o', color='red', markersize=80, zorder=5)

# Label each village with its name
for idx, row in joined.iterrows():
    ax.annotate(f"{row['village_name']}\n({row['district_name']})", (row.geometry.x, row.geometry.y),
                textcoords="offset points", xytext=(5, 5), fontsize=8)
ax.set_title("Villages and Districts with Spatial Join")
plt.show()    