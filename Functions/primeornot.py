'Takes a number as a parameter and check the number is prime or not.'
'NOTE: A prime number is a natural number greater than 1 and'
' that has no positive divisors other than 1 and itself.'

x = int(input("Enter a number:"))
if x > 1:
    for i in range(2, x):
        if (x % i) == 0:
            print("This number", x,"is not a prime number")
            break
    else:
        print("This number", x, "is a prime number")

else:
    print("This number", x, "is not a prime number")