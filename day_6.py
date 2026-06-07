ndvi_data = {"sundarbans":0.82,
            "kolkata urban": 0.12,
            "darjeeling forest": 0.75,
            "hooghly farmland": 0.45,
            "purulia scrubland": 0.28
            }
for loc, ndvi in ndvi_data.items():
    print(f"{loc} -> {ndvi}")
highest_ndvi_location = max(ndvi_data, key=lambda loc: ndvi_data[loc])
print(f"Location with highest NDVI: {highest_ndvi_location}")
lowest_ndvi_location = min(ndvi_data, key=lambda loc: ndvi_data[loc])
print(f"Location with lowest NDVI: {lowest_ndvi_location}")
average_ndvi = sum(ndvi_data.values()) / len(ndvi_data)
print(f"Average NDVI: {average_ndvi}")