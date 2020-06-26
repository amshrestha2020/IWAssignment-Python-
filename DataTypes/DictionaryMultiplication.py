'To generate and print a dictionary that contains a number(between 1 and n)'
'In the form (x, x*x)'
'Sample Dictionary (n = 5)'
'Expected Output: {1:1, 2:4, 3:9, 4:16, 5:25}'

def main():
    squares = {}
    n = int(input("Input a number :"))
    print("Sample Dictionary :", n)
    for x in range(1, n+1):
        squares[x] = x * x
    print("Expected Output :", squares)

if __name__=="__main__":
    main()