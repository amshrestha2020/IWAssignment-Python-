'To square and cube every number in a given list of integers using Lambda'

'Squaring every number in a given list of integers'
lst = [2, 3, 4, 5]
result_square = list(map(lambda n: n * 2, lst))
print(result_square)

'Cubing every number in a given list of integers'
result_cube = list(map(lambda n : n * 3, lst))
print(result_cube)