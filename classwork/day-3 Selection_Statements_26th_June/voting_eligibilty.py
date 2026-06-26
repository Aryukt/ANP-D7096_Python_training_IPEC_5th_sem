'''------------------------------------------------Voting eligibilty----------------------------------------------------
Problem Statement:
Write a program to check a person is eligible for voting or not.
A person is eligible for voting if age is 18 or above.
--------------------------------------------------------------------------------------------------------------------------
'''
#-----------------------------------------------------------------------------------------------------------------------
# taking input from users
age=int(input ("Enter your age: "))
#Validating the age
if age <0:
    exit("age connot be negative")
#checking weather person is eligible for voting
if age>=18:
    print("Person is elgible for voting")
else:
    print("person is not eligible for voting")

#-------------------------------------------------------------------------------------------------------------------------
'''
Output:
Enter your age: 20
Person is elgible for voting
'''