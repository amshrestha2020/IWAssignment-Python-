'Function to sum all the numbers in a list'

list = []
number = int(input('How many numbers to insert in list:'))
for n in range(number):
    numbers = int(input('Enter a number: '))
    list.append(numbers)
print("Sum of all the numbers inserted in a list is: ", sum(list))
