#write a python function to multiply all the numbers in a list

def multiply_list(lst):
    result = 1
    for num in lst:
        result *= num
    return result
numbers = [2, 3, 4]
print("The product of the numbers in the list is:", multiply_list(numbers)) 
