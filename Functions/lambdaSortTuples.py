'To sort a list of tuples using Lambda'

class meat_price():
    meat_price = [('Chicken', 330),('Buff', 500), ('Pork', 350),('Fish', 250)]
    print("Original list of Tuples in random order:")
    print(meat_price)
    meat_price.sort(key = lambda x: x[1])
    print("\n Sorting the list of Tuples into ascending order:")
    print(meat_price)