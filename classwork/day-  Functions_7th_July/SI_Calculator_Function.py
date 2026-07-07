'''WAP to calculate SI'''

#Function to calculate Simple Interest
def Calculate_Simple_Interest(principle,rate,time):
    return principle*rate*time/100
#-----------------------------------------------------
principle=float(input("Enter the principle(in Rs): "))
rate=float(input("Enter the rate of interest (in %): "))
time=int(input("Enter the amount time(in yrs): "))
print("Simple Interest: Rs",Calculate_Simple_Interest(principle,rate,time))