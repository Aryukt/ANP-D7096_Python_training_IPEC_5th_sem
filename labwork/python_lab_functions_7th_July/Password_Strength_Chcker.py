''' Password Strength Checker 
Write a function check_password(password) that checks whether a password is strong. 
A password is considered Strong if: 
• It contains at least 8 characters.  
• It contains at least one uppercase letter.  
• It contains at least one lowercase letter.  
• It contains at least one digit.  The function should return: 
• "Strong Password" 
or  
• "Weak Password"  
The main program should accept a password from the user and display the result. '''
#------------------------------------------------------------------------------------------------
# Function to check password
def check_password(password):
    upper = False
    lower = False
    digit = False
    for ch in password:
        if ch.isupper():
            upper = True
        elif ch.islower():
            lower = True
        elif ch.isdigit():
            digit = True
    if len(password) >= 8 and upper and lower and digit:
        return "Strong Password"
    else:
        return "Weak Password"
# Main Program
password = input("Enter Password: ")
result = check_password(password)
print(result)

'''
Output:
Enter Password: aryukt12S
Strong Password
'''