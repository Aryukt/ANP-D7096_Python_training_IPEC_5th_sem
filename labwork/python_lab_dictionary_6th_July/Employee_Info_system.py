''' Employee Information System 
Problem Statement: 
Create a dictionary where: 
• Employee ID is the key.  
• Value is another dictionary containing:  o Name  o Department  o Salary  Perform the following operations: 
    • Display all employee details.  
    • Search for an employee using Employee ID.  
    • Increase the salary of all employees by 10%.  
    • Display employees belonging to a specific department entered by the user. 
'''
#------------------------------------------------------------------------------------------------
# Employee Information System

# Employee details
employees = {
    1: {"Name": "Manish", "Department": "HR", "Salary": 30000},
    2: {"Name": "Ansh", "Department": "IT", "Salary": 45000},
    3: {"Name": "Samay", "Department": "Finance", "Salary": 40000},
    4: {"Name": "Anishika", "Department": "IT", "Salary": 50000},
    5: {"Name": "Harshita", "Department": "HR", "Salary": 35000}
}

# Display all employee details
print("Employee Details:")
for i in employees:
    print(i, employees[i])

# Search employee by ID
eid = int(input("Enter Employee ID: "))

if eid in employees:
    print("Employee Found:", employees[eid])
else:
    print("Employee Not Found")

# Increase salary by 10%
for i in employees:
    employees[i]["Salary"] = employees[i]["Salary"] + (employees[i]["Salary"] * 10 / 100)

print("Salary Updated:")
for i in employees:
    print(i, employees[i])

# Display employees of a particular department
dept = input("Enter Department: ")

print("Employees in", dept, "Department:")
for i in employees:
    if employees[i]["Department"] == dept:
        print(i, employees[i])

'''
Output:
Employee Details:
1 {'Name': 'Manish', 'Department': 'HR', 'Salary': 30000}
2 {'Name': 'Ansh', 'Department': 'IT', 'Salary': 45000}
3 {'Name': 'Samay', 'Department': 'Finance', 'Salary': 40000}
4 {'Name': 'Anishika', 'Department': 'IT', 'Salary': 50000}
5 {'Name': 'Harshita', 'Department': 'HR', 'Salary': 35000}
Enter Employee ID: 3
Employee Found: {'Name': 'Samay', 'Department': 'Finance', 'Salary': 40000}
Salary Updated:
1 {'Name': 'Manish', 'Department': 'HR', 'Salary': 33000.0}
2 {'Name': 'Ansh', 'Department': 'IT', 'Salary': 49500.0}
3 {'Name': 'Samay', 'Department': 'Finance', 'Salary': 44000.0}
4 {'Name': 'Anishika', 'Department': 'IT', 'Salary': 55000.0}
5 {'Name': 'Harshita', 'Department': 'HR', 'Salary': 38500.0}
Enter Department: IT
Employees in IT Department:
2 {'Name': 'Ansh', 'Department': 'IT', 'Salary': 49500.0}
4 {'Name': 'Anishika', 'Department': 'IT', 'Salary': 55000.0}
'''