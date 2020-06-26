'Create a function that takes one argument'
'And that argument will be multiplied with an unknown given number'

def multiply_func(n):
    return lambda i : i * n

result = multiply_func(1)
print("Multiply 1 with the number 10=", result(10))
result = multiply_func(2)
print("Multiply 2 with the number 10=", result(10))


