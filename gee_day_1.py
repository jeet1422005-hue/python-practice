import ee
ee.Authenticate()
ee.Initialize(project='gee-learning-jeet')

point = ee.Geometry.Point([88.3639, 22.5736])
image = ee.ImageCollection('LANDSAT/LC08/C02/T1_L2') \
    .filterBounds(point) \
    .filterDate('2024-01-01', '2024-03-01') \
    .first()
print(image.getInfo())
