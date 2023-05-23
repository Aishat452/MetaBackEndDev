#local scope 

def get_total(a, b):
    #local variable declared inside a function
    total = a + b
    return total
print(get_total(5, 2))

# Accessing variable outside of the function: 
# print(total)
# Expected Output: NameError: name 'total' is not defined (since total is a local variable)
