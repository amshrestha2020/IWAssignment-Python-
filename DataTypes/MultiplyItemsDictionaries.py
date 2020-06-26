'Program to multiply all the elements in a dictionary'

def main():
    multiply()

def multiply():
    x = {'a': 3, 'g': 2, 'h': 6, 'q': 9}
    print("Dictionary:", x)
    total = 1
    for key in x:
        total = total * x[key]
    print("Multiplying all the elements in a dictionary :", total)

if __name__=="__main__":
    main()