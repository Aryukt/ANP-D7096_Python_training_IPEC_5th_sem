'''Vowel Counter using Function 
Write a Python program that defines a function count_vowels(text). 
The function should: 
• Accept a string.  
• Count the total number of vowels (a, e, i, o, u) irrespective of case.  
• Return the total vowel count.  
The main program should: 
• Accept a sentence from the user.  
• Call the function.  
• Display the total number of vowels. 


Sample Output 
Enter a sentence: 
Python Programming is Fun 
Total Vowels: 6 '''
#------------------------------------------------------------------------------------------------
# Function to count vowels
def count_vowels(text):
    count = 0
    for ch in text:
        if ch.lower() == "a" or ch.lower() == "e" or ch.lower() == "i" or ch.lower() == "o" or ch.lower() == "u":
            count = count + 1
    return count
# Main Program
sentence = input("Enter a sentence: ")
total = count_vowels(sentence)
print("Total Vowels:", total)

'''
Output:
Enter a sentence: are you okay
Total Vowels: 6
'''