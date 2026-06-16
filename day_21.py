import pandas as pd
df ={
    "locations": ["Sundarbans","Darjeeling Forest"," Hooghly Farmland","Kolkata Urban"],
    "ndvi_2020": [0.82, 0.75, 0.45, 0.12],
    "ndvi_2024": [0.74, 0.71, 0.38, 0.09]
}
df = pd.DataFrame(df)
df["ndvi_change"] = df["ndvi_2024"] - df["ndvi_2020"]
def classify_change(change):
    if change > 0:
        return "Increase"
    elif change < 0:
        return "Decrease"
    else:
        return "No Change"
df["change_category"] = df["ndvi_change"].apply(classify_change)
worst = df.loc[df["change_category"].idxmin(), "locations"]
print("Highest Vegitation Loss: " + worst)
print(df)
