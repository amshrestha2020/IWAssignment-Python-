'Create a lambda function that adds 15 to a given number passed in as an argument'
'Also, Create a lambda function that multiplies argument x with argument y and print the result'

def add(n):
    return lambda a : a + n
result = add(15)
print(result(10))

x = lambda a, b : a * b
print(x(3,2))