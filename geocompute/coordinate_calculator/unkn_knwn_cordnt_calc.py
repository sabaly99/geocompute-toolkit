#THIS IS A SIMPLE CODE FOR FINDING COORDINATES GIVEN 
#BEARING BETWEEN THE KNOWN AND THE UNKNOWN POINT 
#AND THE DISTANCE BETWEEN THEM 


import math

def calculator():

    bearing = float(input("INPUT THE BEARING BETWEEN THE 2 POINTS: "))

    N = float(input("INPUT THE NORTHINGS OF THE KNOWN POINT: "))
    E = float(input("INPUT THE EASTINGS OF THE KNOWN POINT: "))
    Distance = float(input("INPUT THE DISTANCE BETWEEN THE 2 POINTS: "))

    Eastings  = E + Distance*math.sin(bearing)
    Northings = N + Distance*math.cos(bearing)

    print(f"THE COORDINATES OF THE UNKNOWN POINT IS N {Eastings} , E {Northings} ")


calculator()
