'Print the even numbers from a given list'

list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

even = [x for x in list if x % 2 == 0]
print("Even numbers from a given list:", even)
