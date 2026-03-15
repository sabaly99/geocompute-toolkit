#CONVERT DMS TO DD
def dms_to_dd():
    Degrees = float(input("enter the degree value : "))
    Minutes = float(input("enter the minutes value : "))
    Seconds = float(input("enter the Seconds value : "))

    print(Degrees + (Minutes/60) + (Seconds/3600))

def DD_to_DMS():
   
   
   DecimalDegrees = float(input("enter the degree value : "))
   Degrees = int(DecimalDegrees)
   Minutes = int((DecimalDegrees - Degrees) * 60)
   Seconds = (DecimalDegrees - Degrees - (Minutes/60)) * 3600
   print(f"{Degrees}, {Minutes}, {round(Seconds,4)}")



print("WHAT ACTION DO YOU WANT TO PERFORM\n")
print("1.DEGREE MINUTES SECONDS --TO-- DECIMAL DEGREE ")
print("2. DECIMAL DEGREE  --TO-- DEGREE MINUTES SECONDS ")

option = int(input("ENTER NUMBER OF ACTION YOU WANT TO PERFORM : "))

if option == 1:
    dms_to_dd()
else:

    DD_to_DMS()

print("OPERATION COMPLETE")