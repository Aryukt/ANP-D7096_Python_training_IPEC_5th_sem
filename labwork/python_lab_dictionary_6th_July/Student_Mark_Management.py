''' Student Marks Management 
Problem Statement: Create a dictionary to store the marks of 5 students, where the key is the student's name and the value is their marks. Perform the following operations: 
• Display all student names and marks.  
• Add a new student with marks.  
• Update the marks of an existing student.  
• Delete a student by name.  
• Display the student who scored the highest marks.  '''
#------------------------------------------------------------------------------------------------
#marks taken from programmer
marks={"Manish":30,"Ansh":25,"Samay":15,"Anishika":28,"Harshita":24}
#Display of marks
print("Marks of students are: ",marks)
#Adding a student and mark 
marks["Disha"]=29
print("New student is added: ",marks)
#Updating the students marks
marks["Anishika"]=20
print("Updated the students marks: ",marks)
#Deleting the students name
del marks["Harshita"]
print("Deleting a students name: ",marks)
#Displaying who scored the highest marks
# 1. Find the highest value in the dictionary
highest_score = max(marks.values())

# 2. Find all keys that have this highest value
top_scorers = [name for name, score in marks.items() if score == highest_score]

# 3. Display the result
print(f"The highest score is {highest_score}.")
print(f"Top scorers: {', '.join(top_scorers)}")   

'''
Output:
Marks of students are:  {'Manish': 30, 'Ansh': 25, 'Samay': 15, 'Anishika': 28, 'Harshita': 24}
New student is added:  {'Manish': 30, 'Ansh': 25, 'Samay': 15, 'Anishika': 28, 'Harshita': 24, 'Disha': 29}
Updated the students marks:  {'Manish': 30, 'Ansh': 25, 'Samay': 15, 'Anishika': 20, 'Harshita': 24, 'Disha': 29}
Deleting a students name:  {'Manish': 30, 'Ansh': 25, 'Samay': 15, 'Anishika': 20, 'Disha': 29}
The highest score is 30.
Top scorers: Manish
'''