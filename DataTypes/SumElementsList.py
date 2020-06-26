'Program to sum all the items in a list.'

list = []
num = int(input('Enter the total number of list elements:'))

def main():
    for n in range(1, num + 1):
         numbers = int(input("Enter the value of element ="))
         list.append(numbers)
    total = sum(list)
    print("The sum of all elements in a given list is :", total)

if __name__=="__main__":
    main()
