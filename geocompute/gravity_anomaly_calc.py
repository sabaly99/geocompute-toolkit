#This is a simple gravity anomaly calculator
#It calculates both free air anomaly and bougrer anomaly
import math 

#These line of code are to take inputs from the user 
grav_obs = float(input("Enter the observed gravity (mgal): "))
H = float(input("Enter the Observed Height(m): "))
Lat = float(input("Enter the latitude (Degrees): "))
density = float(input("Enter the Density(g/cm^3)"))


#We then convert the latitude from degrees to radians for simple calculation
lat_radians = math.radians(Lat)

# This line gives the calculation of normal gravity to be used in the anomaly calculation 
Normal_Gravity = 978032.7 * (1 + 00.0053024 * math.sin(lat_radians)**2 - 0.0000058 * math.sin(2*lat_radians)**2  )


#=== This refers to the Free-Air reduction =====
FAR = 0.3086 * H



#Bougrer reduction
BR = 0.04193 * density * H 


# Free-Air Anomaly
FAA = grav_obs - Normal_Gravity + FAR

#Bougrer Anomaly
BA = FAA - BR
