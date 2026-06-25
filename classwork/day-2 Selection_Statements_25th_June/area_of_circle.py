

radius = float(input("Enter the Radius: "))
# Validating the Radius
if radius < 0 :
    exit("Radius cannot be negative")
#----------------------------------------------
# Display radius
print("Radius: ",radius)
# Display area
print("the area of circle: ",3.14*radius*radius)