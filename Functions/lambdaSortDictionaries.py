'Sort a list of dictionaries using Lambda'

class sort_list():
    list = [{ "name" : "Ram", "age" : 30},
            { "name" : "Hari", "age" : 15},
            { "name" : "Frank", "age" : 28}]

    #using sorted and lamda to print list sorted by age
    sort_list = sorted(list, key = lambda i : i['age'])
    print("Sorting the list of dictionaries by age:")
    print(sort_list)
