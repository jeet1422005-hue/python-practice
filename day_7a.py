districts = {
    "darjeeling": {"area": 3149, "population": 1846823, "forest_cover": 0.68},
    "sundarbans": {"area": 9630, "population": 4500000, "forest_cover":0.82},
    "kolkata": {"area": 185, "population": 14850000, "forest_cover": 0.05},
    "purulia": {"area": 6259, "population":2927965, "forest_cover": 0.23}, 
}
for dist , info in districts.items():
    print(f"{dist}: {info['area']} km², {info['population']} people, {info['forest_cover']*100:.2f}% forest cover")
highest_forest_cover = max(districts, key = lambda dist: districts[dist]["forest_cover"])    
print(f"District with highest forest cover: {highest_forest_cover}")
population_density = {dist: info["population"] / info["area"] for dist, info in districts.items()}
for dist, density in population_density.items():
    print(f"{dist}: {density:.2f} people/km²")
for dist, info in districts.items():
    if info["forest_cover"] > 0.5:
        print(f"{dist} -> Dense forest ")
    elif info["forest_cover"] > 0.2:
        print(f"{dist} -> Moderate forest") 
    else:
        print(f"{dist} -> Sparse forest")            