'''------------------------------------Loan Eligibility Check-------------------------------------------- 
Problem Statement:
A bank considers an applicant eligible for a personal loan only if their monthly salary is ₹30,000 or 
more. 
Write a Python program to accept the applicant's monthly salary and display whether they are 
eligible to apply for the loan. 
---------------------------------------------------------------------------------------------------------
Sample Input 1 
Enter your monthly salary: 45000 
Sample Output 1 
Congratulations! You are eligible to apply for the loan.
---------------------------------------------------------------------------------------------------------- 
Sample Input 2 
Enter your monthly salary: 22000 
Sample Output 2 
Sorry! You are not eligible to apply for the loan. 
----------------------------------------------------------------------------------------------------------
'''
#---------------------------------------------------------------------------------------------------------
#---------------------------------------------Code--------------------------------------------------------

# Taking the input of User
monthly_salary=int(input("Enter your monthly salary: "))
# Validating the monthly salary
if monthly_salary<0:
    exit("Monthly salary cannot be in negative")
# Checking for loan eligibilty
if monthly_salary >=30000:
    print("Congratulations! You are eligible to apply for the loan.")
else:
    print("Sorry! You are not eligible to apply for the loan. ")

#-----------------------------------------------------------------------------------------------------------
'''
Output:
Enter your monthly salary: 32000
Congratulations! You are eligible to apply for the loan.
'''