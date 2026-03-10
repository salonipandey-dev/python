#write a program that accpts a string and count the number of upper case and lower case.
str=input("enter a string: ")
upper=0 
lower=0
for i in str:
    if i.isupper():
        upper+=1
    elif i.islower():
        lower+=1
    else:
        print("not applicable to count")
print("upper case letters: ",upper)
print("lower case letters: ",lower) 

