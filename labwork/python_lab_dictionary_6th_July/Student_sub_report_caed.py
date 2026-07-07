'''Student Subject Report Card 
Problem Statement: 
Create a nested dictionary to store marks of students in three subjects. 
Example: 
{ 
'Rahul': {'Math': 85, 'Science': 90, 'English': 88}, 
'Priya': {'Math': 78, 'Science': 95, 'English': 82}, 
'Ankit': {'Math': 91, 'Science': 89, 'English': 94} 
} 
Write a program to: 
• Calculate the total marks of each student.  
• Calculate the average marks of each student.  
• Display the topper based on total marks.  
• Display the subject-wise highest marks along with the student's name.  
• Display students whose average is greater than or equal to 85.'''
#------------------------------------------------------------------------------------------------
# Student Subject Report Card

# Student marks
students = {
    "Rahul": {"Math": 85, "Science": 90, "English": 88},
    "Priya": {"Math": 78, "Science": 95, "English": 82},
    "Ankit": {"Math": 91, "Science": 89, "English": 94}
}

# Display student details
print("Student Details:")
for name in students:
    print(name, students[name])

# Calculate total and average
print("\nTotal and Average Marks:")
for name in students:
    total = students[name]["Math"] + students[name]["Science"] + students[name]["English"]
    average = total / 3
    print(name, "Total =", total, "Average =", average)

# Display topper
highest = 0
topper = ""

for name in students:
    total = students[name]["Math"] + students[name]["Science"] + students[name]["English"]

    if total > highest:
        highest = total
        topper = name

print("\nTopper is:", topper)
print("Total Marks:", highest)

# Subject-wise highest marks
subjects = ["Math", "Science", "English"]

print("\nSubject-wise Highest Marks:")
for subject in subjects:
    highest = 0
    student = ""

    for name in students:
        if students[name][subject] > highest:
            highest = students[name][subject]
            student = name

    print(subject, ":", highest, "-", student)

# Students having average >= 85
print("\nStudents with Average >= 85:")

for name in students:
    total = students[name]["Math"] + students[name]["Science"] + students[name]["English"]
    average = total / 3

    if average >= 85:
        print(name, "Average =", average)

'''
Output:
Student Details:
Rahul {'Math': 85, 'Science': 90, 'English': 88}
Priya {'Math': 78, 'Science': 95, 'English': 82}
Ankit {'Math': 91, 'Science': 89, 'English': 94}

Total and Average Marks:
Rahul Total = 263 Average = 87.66666666666667
Priya Total = 255 Average = 85.0
Ankit Total = 274 Average = 91.33333333333333

Topper is: Ankit
Total Marks: 274

Subject-wise Highest Marks:
Math : 91 - Ankit
Science : 95 - Priya
English : 94 - Ankit

Students with Average >= 85:
Rahul Average = 87.66666666666667
Priya Average = 85.0
Ankit Average = 91.33333333333333
'''