'Program to insert a given string at the beginning of all items in a list.'
'Sample list: [1, 2, 3, 4], string: emp'
'Expected Output: [emp1, emp2, emp3, emp4]'

def check(list, string):
    string += '{0}'
    list = [string.format(i) for i in list]
    return(list)

list = [1, 2, 3, 4]
print('Sample list :', list)
string = 'emp'
print('String :', string)
print('Expected output :', check(list, string))
