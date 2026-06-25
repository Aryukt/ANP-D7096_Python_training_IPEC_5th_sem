'''Write a program to calculate speed when distance and time has been provided'''
Distance = float(input("enter the distance(in meter): "))
# Validating the Distance
if Distance<0:
    exit("Distance cannot be negative")
Time = float(input("enter the the time(in sec): "))
# Validating the Time
if Time<0:
    exit("Time canot be negative")

#-------------------------------------------

print("--------------------------------------")
#Displaying the Distance 
print("Distance :",Distance)
#Displaying the Time
print("Time",Time)

#Speed
print("Speed(in m/s): ",Distance/Time)
