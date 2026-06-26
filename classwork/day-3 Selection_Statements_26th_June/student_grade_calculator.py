'''-----------------------------------Student Grade Calculator -------------------------------------
A school assigns grades based on the marks obtained by students according to the following criteria: 
• Marks 90 and above → Grade A  
• Marks 75 to 89 → Grade B  
• Marks 50 to 74 → Grade C  
• Below 50 → Grade F  

Write a Python program to accept marks from the user and display the corresponding grade. 
----------------------------------------------------------------------------------------------------
Sample Input 
Enter Marks: 92 
Sample Output 
Grade A 
-----------------------------------------------------------------------------------------------------
Sample Input 
Enter Marks: 80 
Sample Output 
Grade B 
-----------------------------------------------------------------------------------------------------
Sample Input 
Enter Marks: 65 
Sample Output 
Grade C 
-----------------------------------------------------------------------------------------------------
Sample Input 
Enter Marks: 35 
Sample Output 
Grade F
------------------------------------------------------------------------------------------------------
'''
#----------------------------------------------------------------------------------------------------
#-----------------------------------------Coding-----------------------------------------------------
marks = int(input("Enter your marks: "))
# validating the marks
if(marks<0&marks>100):
    exit("marks cannot be in negative and grater than 100")


