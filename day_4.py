cities = {"delhi": 42,
          "mumbai": 35,
          "darjeeling":18,
          "jaipur":45,
          "kolkata":38}
for city , temp  in cities.items():
    print (city + " -> " + str(temp) + "*C")
print("\nHotest cities")
for city, temp in cities.items():
    if temp > 40:
        print (city + " -> " + str(temp) +"*C")
Hotest_city = max(cities, key=lambda city: cities[city])
print ("Hotest City:"+ Hotest_city)
Coldest_city = min(cities, key=lambda city:cities[city])
print ("Coldest City:"+ Coldest_city)
average = sum(cities.values())/len(cities)
print ("Avg Temp:" + str(average)+ "*C")
