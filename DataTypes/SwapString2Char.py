'Program to get a single string from two given strings'
'separated by a space and swap the first two characters of each string'
'Sample String: abc xyz'
'Expected Result: xyc abz'

def main():
    a = input("Enter First String:")
    b = input("Enter Second String:")

    new_a = b[:2] + a[2:]
    new_b = a[:2] + b[2:]

    print("The new string after swapping first two characters of both string:",
          (new_a+ '' +new_b))

if __name__ == '__main__':
    main()
