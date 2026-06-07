import csv

with open ("py_pr_cgpt/rivers.csv","r")as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        river,leangth_km,basin_area,polution_level = row
        print(f"{river}: {leangth_km} km, {basin_area} km*2, {float(polution_level)*100:.2f}% polution level")
river_data ={}
with open ("py_pr_cgpt/rivers.csv","r")as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        river,leangth_km,basin_area,polution_level = row
        river_data[river] = {"length_km": int(leangth_km), "basin_area": int(basin_area), "polution_level": float(polution_level)}
most_polluted_river = max(river_data, key=lambda r: river_data[r]["polution_level"])
count = sum(1 for r in river_data if river_data[r]["polution_level"] > 0.5)
print(f"Most polluted river: {most_polluted_river}")
print(f"Number of rivers with pollution level above 0.5: {count}")        