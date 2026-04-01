marks=[]
for i in range(1, 7):
    mark=int(input("Enter the marks of student: "))
    marks.append(mark)
marks.sort()
print("The marks of students in sorted order are:", marks)