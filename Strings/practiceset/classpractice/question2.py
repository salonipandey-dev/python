#write a py function that checks a whether a passed strign a palindrime or not.
def is_palindrome(s):
    return s[::-1]
str=input("enter a string: ")
if is_palindrome(str):
    print("the string is a palindrome") 
else:  
    print("the string is not a palindrome")
