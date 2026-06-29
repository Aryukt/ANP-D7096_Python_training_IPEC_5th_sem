'''
Login System with Maximum Attempts
Problem Statement
A system allows only three login attempts.
The correct username is admin and the password is python123.
If the credentials are correct, display "Login Successful".
Otherwise, after three unsuccessful attempts, display "Account Locked".
Sample Output
Attempt 1
Username: admin
Password: abc
Invalid Credentials
Attempt 2
Username: admin
Password: python123
Login Successful'''
username = "admin"
password = "python123"
attempts = 0
while attempts < 3:
    user_input = input("Username: ")
    pass_input = input("Password: ")
    if user_input == username and pass_input == password:
        print("Login Successful")
        break
    else:
        print("Invalid Credentials")
        attempts += 1
if attempts == 3:
    print("Account Locked") 
    