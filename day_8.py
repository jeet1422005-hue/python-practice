import csv
with open("wb_districts.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["District", "Area", "Population", "Forest Cover"])
    writer.writerow(["Darjeeling", 3149, 1846823, 0.68])
    writer.writerow(["Sundarbans", 9630, 4500000, 0.82])
    writer.writerow(["Kolkata", 185, 14850000, 0.05])
    writer.writerow(["Purulia", 6259, 2927965, 0.23])
with open("wb_districts.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header
    for row in reader:
        district, area, population, forest_cover = row
        print(f"{district}: {area} km², {population} people, {float(forest_cover)*100:.2f}% forest cover")

   