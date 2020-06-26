'Check whether a given key already exists in a dictionary'

b = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60, 7: 70, 8: 80}
print("list of Keys :", b)
y = int(input("Enter a number :"))

def key_present(y):
    if y in b:
        print("Given key already exists in a dictionary")
    else:
        print("Given key does not exist in a dictionary")

key_present(y)
