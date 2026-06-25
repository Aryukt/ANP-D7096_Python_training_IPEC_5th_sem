length = float(input("Enter length: "))
# Validating the length
if length<0:
    exit("length of rectangle cannot be zero")
width = float(input("Enter width: "))
# Validating the width
if width<0:
    exit("Width of rectangle cannot be zero")
#-----------------------------------------------
print("-----------------------------------------")
#Displaying the length and width
print("Length: ",length)
print("Width: ",width)


# Displaying area and perimeter
print("Area =", length*width)
print("Perimeter =", 2*(length+width))