'Program to change a given string to a new string where the first and last chars have been exchanged'

def main():
    w = input("Enter a string:")
    print("String after swapping first and last character:",
          (w[-1:] + w[1:-1] + w[:1]))

if __name__=="__main__":
    main()