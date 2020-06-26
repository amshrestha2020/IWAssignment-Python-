'Program to check whether all dictionaries in a list are empty or not.'
'Sample list: [{}, {}, {}]'
'Return value: True'
'Sample list: [{1,2}, {}, {}]'
'Return value: False'

sample_list1 = [{}, {}, {}]
sample_list2 = [{1}, {}, {}]

print(all(not d for d in sample_list1))
print(all(not d for d in sample_list2))


