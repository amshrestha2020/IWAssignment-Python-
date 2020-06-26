'Program to remove a key from a dictionary'

def main():
    remove()

def remove():
    x = {'a': 3, 'g': 2, 'h': 6, 'q': 9}
    print("Dictionary Items :", x)

    key = input("Enter a key that you want to remove :")

    if key in x:
        del x[key]
    else:
        print("Given key is not is in this dictionary items.")
    print("Updated Dictionary =", x)

if __name__=="__main__":
    main()