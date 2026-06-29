'''
Electricity Bill Analysis
Problem Statement
An electricity department wants to analyze electricity consumption of N houses.
Accept the monthly units consumed by each house.
Calculate and display:
• Total units consumed
• Average units consumed
• Highest consumption
• Lowest consumption'''
n = int(input("Enter the number of houses: "))
units = []
for i in range(n):
    unit = float(input(f"Enter units consumed by house {i + 1}: "))
    units.append(unit)

total_units = sum(units)
average_units = total_units / n if n > 0 else 0
highest_consumption = max(units) if units else 0
lowest_consumption = min(units) if units else 0

print(f"Total units consumed: {total_units}")
print(f"Average units consumed: {average_units}")
print(f"Highest consumption: {highest_consumption}")
print(f"Lowest consumption: {lowest_consumption}")