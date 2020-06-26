'Program to multiplies all the items in a list.'

def main():
    multiply_list()

def multiply_list():
    list = []
    for i in range(1, 5):
        list.append(i)
    print(list)
    result = 1
    for item in list:
        result = result * item
    print("Multiplies all the items in a list :",result)

if __name__=="__main__":
    main()