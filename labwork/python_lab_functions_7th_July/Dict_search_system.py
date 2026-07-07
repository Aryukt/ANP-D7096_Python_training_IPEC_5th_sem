'''Dictionary Search System 
Write a Python program that defines a function search_student(student_dict, roll_no). 
The function should: 
• Accept a dictionary where:  
o Key = Roll Number  
o Value = Student Name  
• Search for the given roll number.  
• Return the student name if found; otherwise return "Student Not Found".  
The main program should: 
• Create a dictionary of at least 5 students.  
• Accept a roll number from the user.  
• Display the search result. '''
#------------------------------------------------------------------------------------------------
# Function to search student
def search_student(student_dict, roll_no):
    if roll_no in student_dict:
        return student_dict[roll_no]
    else:
        return "Student Not Found"
# Main Program
students = {
    101: "Manish",
    102: "Ansh",
    103: "Samay",
    104: "Anishika",
    105: "Harshita"
}
print("Student Dictionary:", students)
roll = int(input("Enter Roll Number: "))
result = search_student(students, roll)
print("Search Result:", result)

'''
Output:
Student Dictionary: {101: 'Manish', 102: 'Ansh', 103: 'Samay', 104: 'Anishika', 105: 'Harshita'}
Enter Roll Number: 105
Search Result: Harshita
'''