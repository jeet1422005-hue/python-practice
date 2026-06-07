rivers= {
    "ganga": {"length_km": 520, "basin_area":9800, "polution_level": 0.78 },
    "damodar": {"length_km": 592, "basin_area": 2200, "polution_level": 0.85},
    "teesta": {"length_km": 315, "basin_area": 1800, "polution_level": 0.32},
    "rupnarayan": {"length_km": 160, "basin_area":950, "polution_level": 0.45}
}
for riv, info in rivers.items():
    print(f"{riv}: {info['length_km']} km, basin area: {info['basin_area']} km², pollution level: {info['polution_level']*100:.2f}%")
most_polluted_river = max(rivers, key=lambda riv: rivers[riv]["polution_level"])
print(f"Most polluted river: {most_polluted_river}")    
for riv, info in rivers.items():
    if info["polution_level"] > 0.7:
        print(f"{riv} -> Critically polluted")
    elif info["polution_level"] > 0.4:
        print(f"{riv} -> Moderately polluted")
    else:
        print(f"{riv} -> Relatively Clean")
average_pollution = sum(info["polution_level"] for info in rivers.values()) / len(rivers)
print(f"Average pollution level: {average_pollution*100:.2f}%")