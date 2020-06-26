'Program to get the smallest number from a list'

def main():
    h = input("Enter an integer for list(space separated):")
    p = list(map(int, h.split()))
    print("The smallest number from a list:", min(p))

if __name__=="__main__":
    main()