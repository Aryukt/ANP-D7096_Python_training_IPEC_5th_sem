'''
 Employee Salary Statistics
Problem Statement
A company has N employees.
Accept the salary of each employee and determine:
• Highest salary
• Lowest salary
• Average salary
• Number of employees earning more than ₹50,000'''
n = int(input("Enter the number of employees: "))
salaries = []
for i in range(n):
    salary = float(input(f"Enter salary of employee {i + 1}: "))
    salaries.append(salary)

highest_salary = max(salaries)
lowest_salary = min(salaries)
average_salary = sum(salaries) / len(salaries) if salaries else 0
employees_above_50k = len([salary for salary in salaries if salary > 50000])

print(f"Highest salary: ₹{highest_salary}")
print(f"Lowest salary: ₹{lowest_salary}")
print(f"Average salary: ₹{average_salary}")
print(f"Number of employees earning more than ₹50,000: {employees_above_50k}")
