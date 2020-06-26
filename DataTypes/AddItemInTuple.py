'Program to add an item in a tuple'

def main():
    add_item()

def add_item():
    x = (1, 2, 3)
    print("Original Tuple:", x)

    a = 2
    x = x[ :a] + (9 ,) + x[a: ]

    print("Added an item in a tuple :", x)

if __name__=="__main__":
    main()