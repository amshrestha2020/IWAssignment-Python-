'Filter a list of integers using Lambda'

lst = [2, 3, 4, 5]

'use anonymous function to filter and comparing'
'if divisible or not'
result = list( filter ( lambda n : (n % 2 == 0), lst))
print(result)