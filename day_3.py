states = {"uttar pradesh": 23,
          "maharashtra":12,
          "west bengal":9,
          "rajasthan":8,
          "goa":0.15}
for state , pop in states.items():
    print(state + " -> " + str(pop) + "cr")
    print("\nStates over 5 cr population")
    for state , pop in states.items():
        if pop > 5:
            print(state + " -> "+ str(pop)+"cr")
most_populated = max(states,key=lambda state: states[state])
print("most_populated:" + most_populated)
least_populated= min(states, key=lambda state: states[state])
print("least_populated:"+ least_populated)