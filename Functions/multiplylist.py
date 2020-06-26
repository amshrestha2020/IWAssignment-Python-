'Multiply all the numbers in a list'

def multiply(numbers):
    total = 1
    for i in numbers:
        total *= i
    return total
print(multiply((8, 2, 3, -1, 7)))