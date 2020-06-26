'Program to convert a list to a tuple'

def main():
    convert_list()

def convert_list():
    x = ['Apple', 'Samsung', 'Motorola']
    a = tuple(x)

    print("List :", x)
    print("Converted a list to a tuple :", a)

if __name__=="__main__":
    main()