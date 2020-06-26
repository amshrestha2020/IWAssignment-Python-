'Program to convert a tuple into string'

def main():
    convert_tuple()

def convert_tuple():
    x = ('P', 'y', 't', 'h', 'o', 'n')
    a = ''
    for item in x:
        a = a + item

    print("Tuples :", x)
    print("Converted a tuple into string :",a)

if __name__=="__main__":
    main()