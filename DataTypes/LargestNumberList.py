'Program to get the largest number from a list'

def main():
    h = input("Enter an integer number in list(space separated):")
    p = list(map(int, h.split()))
    print("The largest number from a list:", max(p))

if __name__=="__main__":
    main()