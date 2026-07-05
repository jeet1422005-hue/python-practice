import geopandas as gpd

# Load directly from the internet - no file needed
india = gpd.read_file("https://github.com/datameet/maps/raw/master/Districts/Census_2011/2011_Dist.shp")

print(india.shape)
print(india.columns.tolist())
print(india.head(3))

# Filter for West Bengal only
wb = india[india['ST_NM'] == 'West Bengal']

print(wb.shape)
print(wb['DISTRICT'].tolist())

import matplotlib.pyplot as plt

wb.plot(edgecolor='black', color='lightgreen')
plt.title("West Bengal Districts")
plt.show()

# Highlight Murshidabad
murshidabad = wb[wb['DISTRICT'] == 'Murshidabad']

fig, ax = plt.subplots(figsize=(8, 10))

# All WB districts in light green
wb.plot(ax=ax, edgecolor='black', color='lightgreen')

# Murshidabad highlighted in red
murshidabad.plot(ax=ax, edgecolor='black', color='red', alpha=0.7)

plt.title("West Bengal Districts - Murshidabad Highlighted")
plt.show()