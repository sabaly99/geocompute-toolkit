import math


def dist_bear():
    
    points = int(input("ENTER THE TOTAL NUMBER OF INTRUMENT READINGS TAKEN : "))

		
    east_control = float(input("Enter the eastings of the control: "))
    nort_control = float(input("Enter the northings of the control: "))



    for i in range(1 , points + 1):

        eastings = float(input(f"Enter the eastings of point {i} "))

        northings = float(input(f"Enter the northing of point {i} "))
	 
        

        ch_eastings = east_control - eastings
        
        ch_northings=nort_control-northings 
			
        distance = math.sqrt(ch_eastings**2 + ch_northings**2)

			
        bearing_Rad = math.atan(ch_eastings/ch_northings)
        bearing_degree = math.degrees(bearing_Rad)

        Degrees = int(bearing_degree)
        Minutes = int((bearing_degree - Degrees) * 60)
        Seconds = (bearing_degree - Degrees - (Minutes/60)) * 3600
       # print(Degrees, Minutes, Seconds.round(4))
			
       
       
        print(f"THE DISTANCE AND BEARING OF POINT {i} is  {distance}m , {Degrees, Minutes, round(Seconds,4)}" )

#LINE TO SHOW THE CALCULATION DONE
    print("COMPUTATION complete") 




#FINALLY CODE TO CALL THE FUNCTION TO WORK
dist_bear()