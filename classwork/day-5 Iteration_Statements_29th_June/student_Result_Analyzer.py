'''
Student Result Analyzer
Problem Statement
A teacher wants to analyze the marks of N students.
Accept the marks of each student (out of 100).
Finally display:
• Highest Marks
• Lowest Marks
• Average Marks
• Number of students who passed (Marks ≥ 40)
• Number of students who scored distinction (Marks ≥ 75)'''
N = int(input("Enter the number of students: ")) 
# Entering 5, then it will take 5 students
marks = []
# Creating empty list
for i in range(N):
    mark = float(input(f"Enter marks of student {i + 1} (out of 100): "))
    marks.append(mark)
# Ex- marks=[50,60,75,90,35]
highest_marks = max(marks)
lowest_marks = min(marks)
average_marks = sum(marks) / len(marks) if marks else 0
passed_students = len([mark for mark in marks if mark >= 40])
distinction_students = len([mark for mark in marks if mark >= 75])

print(f"Highest Marks: {highest_marks}")
print(f"Lowest Marks: {lowest_marks}")
print(f"Average Marks: {average_marks}")
print(f"Number of students who passed: {passed_students}")
print(f"Number of students who scored distinction: {distinction_students}")
