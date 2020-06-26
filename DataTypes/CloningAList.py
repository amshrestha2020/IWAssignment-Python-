'Program to clone or copy a list'

def main():
    x = input("Enter a list(space separated):")

    b = list(x.split())
    new_b = list(b)

    print("Old list:", b)
    print("Clone or copy a list:", new_b)

if __name__=="__main__":
    main()