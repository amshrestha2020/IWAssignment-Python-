'Program to remove the nth index character from a nonempty string'

def main():
    y = input("Enter a string:")
    f = int(input("Enter the index position of the character to be removed:"))

    first_part = y[:f-1]
    last_part = y[f:]

    print("The new string after removing the nth index character:",
          (first_part + last_part))

if __name__=="__main__":
    main()