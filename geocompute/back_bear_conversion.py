def back_bearing():

    bearing = float(input("enter the bearing: "))
    N_bearing = bearing % 360

    if N_bearing > 180:
        new_bear = N_bearing - 180
    elif:
        new_bear = N_bearing + 180

    return(new_bear)


value = back_bearing()
print(value)