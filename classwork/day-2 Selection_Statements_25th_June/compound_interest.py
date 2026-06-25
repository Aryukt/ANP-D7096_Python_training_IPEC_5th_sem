Principle = float(input("Enter principal amount(Rs): "))
# Validating the principle
if Principle<0:
    exit("Principle cannot be zero")
Rate = float(input("Enter rate of interest(%): "))
# Validating the Rate of Interest
if Rate<0:
    exit("Rate of interest cannot be zero")
Time = float(input("Enter time (years): "))
# Validating the Time
if Time<0:
    exit("Time cannot be zero")

Amount = Principle * (1 + Rate / 100) ** Time

print("Amount =",Amount)
print("Compound Interest =", Amount - Principle)