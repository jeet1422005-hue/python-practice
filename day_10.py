import csv
with open("py_pr_cgpt/wb_climate_new.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        station,district,elevation_m,avg_rainfall_mm,avg_temp_c = row
        print(f"{station}: elevation {elevation_m} M, average rainfall {avg_rainfall_mm}mm")
climate_data = {}
with open("py_pr_cgpt/wb_climate_new.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        station,district,elevation_m,avg_rainfall_mm,avg_temp_c = row
        climate_data[station] = {
            "rainfall": float(avg_rainfall_mm),
            "temperature": float(avg_temp_c),
            "elevation": int(elevation_m)
        }
highest_rainfall_station = max(climate_data, key=lambda s: climate_data[s]["rainfall"])
print(f"Station with highest average rainfall: {highest_rainfall_station} ({climate_data[highest_rainfall_station]['rainfall']} mm)")
lowest_temp_station = min(climate_data, key=lambda s: climate_data[s]["temperature"])
print(f"Station with lowest average temperature: {lowest_temp_station} ({climate_data[lowest_temp_station]['temperature']} °C)")
for station, data in climate_data.items():
    if data["elevation"] > 1000:
        print(f"{station} is at a high elevation of {data['elevation']} M")
    elif data["elevation"] > 500:
        print(f"{station} is at a moderate elevation of {data['elevation']} M")
    else:
        print(f"{station} is at a low elevation of {data['elevation']} M")        