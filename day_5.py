wb_ndvi = {"sundarbans": 0.82,
           "kolkata urban": 0.12,
           "darjeeling forest": 0.75,
           "hooghly farmland": 0.45,
           "purulia scrumbland": 0.28
           }
for location , ndvi in wb_ndvi.items():
    print(location + " -> " + str(ndvi))
for location ,ndvi in wb_ndvi.items():
    if ndvi > 0.6:
        print (location + ":" + "Dense Vegetation")
    elif ndvi > 0.3:
        print (location + ":" + "Moderate Vegetaion")
    else:
        print (location + ":" + "Bare/Spare")     
count = 0
for location , ndvi in wb_ndvi.items():
    if ndvi > 0.6:
        count += 1
print("Number of locations with Dense Vegetation:", str(count))