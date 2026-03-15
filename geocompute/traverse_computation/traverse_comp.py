import math 



def trav_comp():

    stations = int(input("ENTER THE NUMBER OF OBSERVATIONS MADE: "))
    BEARING = float(input("ENTER THE BEARING OF THE DEPARTURE LINE: "))


    def back_bear():

        bearing = float(input("enter the bearing the previous line: "))
        N_bearing = bearing % 360

        if N_bearing > 180:
            new_bear = N_bearing - 180
        elif N_bearing < 180:
            new_bear = N_bearing + 180
        else:
            return 0

        return(new_bear)


    


    for i in range(1 , stations + 1):

        BACK_BEARING = back_bear()


        included_angle = float(input(f"ENTER THE INCLUDED ANGLE FOR obs{i}: "))
        BACK_BEARING = included_angle + BACK_BEARING


        print(f"BEARING OF LINE {i} : {BACK_BEARING} degrees")



trav_comp()


        
