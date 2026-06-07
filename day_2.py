rivers =  [
    ["ganga",2525 ],
    ["godavari",1465 ],
    ["yamuna",1376],
    ["narmada",1312 ],
    ["teesta", 309]
    ]
#rivers.sort(key=lambda river: river[1],reverse= True)
#for river in rivers:
#    print(river[0]+" -> "+str(river[1])+"km")
#print("Longest:" + rivers[0][0]+" -> " + str(rivers[0][1]) +"km")
#print("Shortest:"+ rivers[-1][0] + " -> "+ str(rivers[-1][1])+ "km")
for river in rivers:
    if river[1] > 1000:
     print(river[0]+ " -> "+str(river[1])+ "km")