'''List Analysis using Functions
Write a Python program that defines the following functions: 
• find_max(numbers)  
• find_min(numbers)  
• find_average(numbers)  
The program should: 
• Accept a list of 10 integers from the user.  
• Call all three functions.  
• Display the maximum value, minimum value, and average of the list.  
'''
#--------------------------------------------------------------------------------------------------------------------------
def Calculate_max(numbers):
    return max(numbers)
def Calculate_min(numbers):
    return min(numbers)
def Calculate_average(numbers):
    return sum(numbers)/len(numbers)

#Main Program

numbers=[]
for x in range(10):
    num=int(input("Enter the numbers: "))
    numbers.append(num)
print("the maximum value: ",Calculate_max(numbers))
print("the minimun value: ",Calculate_min(numbers))
print("the average value: ",Calculate_average(numbers))
'''
Output:
Enter the numbers: 23
Enter the numbers: 1
Enter the numbers: 2
Enter the numbers: 3
Enter the numbers: 4
Enter the numbers: 34
Enter the numbers: 25
Enter the numbers: 56
Enter the numbers: 6
Enter the numbers: 4
the maximum value:  56
the minimun value:  1
the average value:  15.8
'''