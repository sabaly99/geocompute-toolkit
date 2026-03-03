def leveling_calculator():

    BS = float(input("INPUT YOUR BACK SIGHT READING : "))
    RL_BENCHMARK = float(input("INPUT THE REDUCED LEVEL OF BENCHMARK : "))

    INS_HEIGHT = BS + RL_BENCHMARK

    points = int(input("ENTER THE TOTAL NUMBER OF INTRUMENT READINGS TAKEN : "))
    

    for i in range(1 , points + 1):

        FS = float(input("ENTER YOUR BACK SIGHT READING: "))
        REDUCED_LEVEL = INS_HEIGHT - FS
        print(F"REDUCED LEVEL OF POINT {i} IS {REDUCED_LEVEL} m" )


    print("LEVELING COMPUTATION COMPLETE")



leveling_calculator()


