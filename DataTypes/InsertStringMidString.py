'Function to insert a string in the middle of a string'
'Sample function and result:'
'insert_sting_middle([[]]<<>>, Python) -> [[Python]]'
'insert_sting_middle({{}}, PHP) -> {{PHP}}'

def insertStringMidString(a, x):
    return a[:2] + x + a[2:]

print(insertStringMidString('[[]]', 'Python'))
print(insertStringMidString('{{}}', 'PHP'))
print(insertStringMidString('<<>>', 'Python'))
