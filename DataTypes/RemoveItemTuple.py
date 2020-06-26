'Program to remove an item from a tuple'

def main():
    remove_item()

def remove_item():
    x = (1, 2, 3, 'apple', 4, 5, 6)
    print("Tuple :", x)

    n = 3
    x = x[ :n] + x[n+1: ]
    print("Removed an item from a tuple :", x)

if __name__=="__main__":
    main()