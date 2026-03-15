import math 

def trav_comp():

    stations = float(input("ENTER THE NUMBER OF OBSERVATIONS MADE: "))
    BEARING = float(input("ENTER THE BEARING OF THE DEPARTURE LINE: "))


    def back_bear():

    bearing = float(input("enter the bearing: "))
    N_bearing = bearing % 360

    if N_bearing > 180:
        new_bear = N_bearing - 180
    elif:
        new_bear = N_bearing + 180

    return(new_bear)

    BACK_BEARING = back_bear



    for i in  range(stations + 1):

        included_angle = float(input(f"ENTER THE INCLUDED ANGLE FOR obs{i}: "))
        CALCULATED_BEARING = included_angle + 

        
