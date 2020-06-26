'Program to unpack a tuple in several variables'

def main():
    unpack_tuple()

def unpack_tuple():
    x, *y, z = (5, "Python", "Django" )

    print(x)
    print(y)
    print(z)

if __name__=="__main__":
    main()