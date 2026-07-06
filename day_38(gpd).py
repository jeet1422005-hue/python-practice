import geopandas as gpd
import matplotlib.pyplot as plt

# Load and filter (same as Day 7)
india = gpd.read_file("https://github.com/datameet/maps/raw/master/Districts/Census_2011/2011_Dist.shp")
wb = india[india['ST_NM'] == 'West Bengal']

fig, ax = plt.subplots(figsize=(10, 12))
wb.plot(ax=ax, edgecolor='black', color='lightgreen')

# Label every district
for idx, row in wb.iterrows():
    ax.annotate(row['DISTRICT'], 
                xy=(row.geometry.centroid.x, row.geometry.centroid.y),
                fontsize=7, ha='center')

plt.title("West Bengal - All Districts Labeled")
plt.show()

# Reproject to UTM for accurate area in km²
wb_utm = wb.to_crs("EPSG:32645")

# Calculate area in km² for each district
wb_utm['area_km2'] = wb_utm.geometry.area / 1_000_000

# Print sorted by area
print(wb_utm[['DISTRICT', 'area_km2']].sort_values('area_km2', ascending=False))

# Find districts that border Murshidabad
murshidabad_geom = wb_utm[wb_utm['DISTRICT'] == 'Murshidabad'].geometry.iloc[0]

neighbors = wb_utm[wb_utm.geometry.touches(murshidabad_geom)]
print("\nDistricts bordering Murshidabad:")
print(neighbors['DISTRICT'].tolist())