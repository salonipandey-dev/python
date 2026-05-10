# program to get even numbers from 1 to n
n= int(input("enter the number:"))
for i in range(2,n+1, 2):
     print(i) 

#program to get odd from 1 to n
n = int(input("enter the number:"))
for i in range(1, n+1,2):
     print(i) 

#program to get even and odd numbers from 1 to n
n = int(input("enter the number:"))
for i in range(1,n+1):
    if i%2==0:
        print(i,"is even")
    else:
        print(i,"is odd")

#program to get even and odd through function
def even_odd(n):
    for i in range(1, n+1):
            if i%2==0:
               print(i,"is even")
            else:
               print(i,"is odd")   
n = int(input("enter the number:"))
even_odd(n)