'''Student Grade Calculator
Write a Python program that defines a function calculate_grade(marks). 
The function should: 
• Accept marks (0–100) as a parameter.  
• Return the grade according to the following criteria:  
o 90 and above → A+  
o 75–89 → A  
o 60–74 → B  
o 40–59 → C  
o Below 40 → Fail  T
he main program should: 
• Accept marks of 5 students.  
• Call the function for each student.  
• Display the marks and corresponding grade.  '''
#---------------------------------------------------------------------------------------------------------------------------
def Display_Students_Grade(marks):
    if (marks>90):
        print("Marks:",marks,"Grade: A+")
    elif(marks>75):
        print("Marks:",marks,"Grade: A")
    elif(marks>60):
        print("Marks:",marks,"Grade: B")
    elif(marks>40):
        print("Marks:",marks,"Grade: c")
    else:
        print("Fail")
#Main Program
marks=int(input("Enter the marks: "))
#Validating the marks
if(marks>100 or marks<0):
    print("Marks are invalid")
else:
    Display_Students_Grade(marks)
#------------------------------------------------------------------------------------------------------------------------------
'''
Output:
Enter the marks: 50
Marks: 50 Grade: c
'''


