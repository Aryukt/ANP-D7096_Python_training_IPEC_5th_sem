'''------------------------------------------Smart Income Tax Calculator--------------------------------------------- 
Problem Statement:
A government tax portal calculates tax based on the following conditions: 
• Income up to ₹5,00,000 → No tax  
• ₹5,00,001 to ₹10,00,000 → 10%  
• ₹10,00,001 to ₹20,00,000 → 20%  
• Above ₹20,00,000 → 30%  
Additional Benefits: 
• Senior citizens (Age ≥ 60) receive a 5% rebate on tax.  
• Women taxpayers receive an additional 2% rebate on tax.  
Write a Python program to calculate the final tax amount payable. 
---------------------------------------------------------------------------------------------------------------------
Sample Input 
Enter Annual Income: 1200000 
Enter Age: 65 
Enter Gender (M/F): F 
Sample Output 
Tax before rebate: ₹240000.0 
Senior Citizen Rebate: ₹12000.0 
Women Rebate: ₹4800.0 
Final Tax Payable: ₹223200.0
----------------------------------------------------------------------------------------------------------------------'''
#------------------------------------------------------------------------------------------------------------------------

annual_income=int(input("Enter Annual Income: "))
age = int(input("Enter Age: "))
gender = input("Enter Gender (M/F): ")
#Validating your annual income
if annual_income<0:
    exit("Annual Income cannot be negative")
#Validating your age
if age<0:
    exit("Age cannot be negative")
#Checking for annual income
if annual_income<500000:
    print("No Tax")
    exit()
elif annual_income >500000 and annual_income<1000000:
    tax = annual_income * 0.1
    
elif annual_income >1000000 and annual_income<2000000:
    tax = annual_income * 0.2
   
else:
    tax = annual_income * 0.3
print("Tax before Rebate: ",tax)
rebate=0
women_rebate=0
#rebate for senior citizen and women
if (age>=60):
    rebate=annual_income*0.05
    print("Senior Citizen Rebate: ",rebate)
if gender == "F":
    women_rebate=annual_income*0.02
    print("Women Rebate: ",women_rebate)
final_tax = tax - rebate - women_rebate
print("Final tax payable: ",final_tax)