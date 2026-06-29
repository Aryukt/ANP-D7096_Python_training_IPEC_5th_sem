'''
Count Prime Numbers in a Range
Problem Statement
Accept two integers representing the starting and ending values of a range.
Display all prime numbers within the range and finally display the total number of prime numbers
found'''
start = int(input("Enter the starting value: "))
end = int(input("Enter the ending value: "))
count = 0
for num in range(start, end + 1):
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if (num % i) == 0:
                break
        else:
            print(num)
            count += 1
print(f"Total prime numbers found: {count}")
