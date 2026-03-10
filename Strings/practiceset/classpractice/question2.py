#write a py function that checks a whether a passed strign a palindrime or not.

str=input("enter a string: ")
if str==str[::-1]:
    print("the string is a palindrome") 
else:  
    print("the string is not a palindrome")
