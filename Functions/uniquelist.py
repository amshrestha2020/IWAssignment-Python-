'Takes a list and returns a new list with unique elements of the first list'

def unique(list):
    unique_list = []

    for x in list:
        if x not in unique_list:
            unique_list.append(x)

    for x in unique_list:
        print(x)

list = [1, 2, 3, 3, 3, 3, 4, 5]
print("The unique values from list:")
unique(list)