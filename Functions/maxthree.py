'Find the Max of three numbers'

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))

if (a >= b) and (a >= c):
   largestnumber = a
elif (b >= a) and (b >= c):
   largestnumber = b
else:
   largestnumber = c

print("The largest number among", a,",", b,"and", c,"is: ",largestnumber)