#write a py function that takes a list and return a new list wiht different elements of the first list.

def Different(lst):
    return list(set(lst))   
numbers = [1, 2, 3, 4, 5, 2, 3, 6]
print("The different elements in the list are:", Different(numbers))
