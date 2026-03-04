import math


def dist_bear():
    
    points = int(input("ENTER THE TOTAL NUMBER OF INTRUMENT READINGS TAKEN : "))

		
    east_control = float(input("Enter the eastings of the control: "))
    nort_control = float(input("Enter the northings of the control: "))



    for i in range(1 , points + 1):

        northings = float(input("Enter the northing of point i "))
	 
        eastings = float(input("Enter the eastings of point i "))

        ch_eastings = east_control - eastings
        
        ch_northings=nort_control-northings 
			
        distance = math.sqrt(ch_eastings/ch_northings)
			
        bearing = math.atan(ch_eastings/ch_northings)
			
        bearing_degree = math.degrees(bearing)
       
        print(f"THE DISTANCE AND BEARING OF POINT {i} is  {distance}m , {bearing_degree}" )

#LINE TO SHOW THE CALCULATION DONE
    print("COMPUTATION complete") 




#FINALLY CODE TO CALL THE FUNCTION TO WORK
dist_bear()