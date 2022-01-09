d=int(input("distance between the two cities in KM: "))

d1=d*1000 #in meter 
d2=d*3280.84 #in feet
d3=d*39370.079 #in inch
d4=d*100000 #in cm

print("distance in meter is : ",d1)
print("distance in feet is : ",d2)
print("distance in inch is : ",d3)
print("distance in centimeter is : ",d4)