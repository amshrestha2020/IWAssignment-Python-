'Program to get a string made of the first 2 and the last 2 chars from a given a string.'
'If the string length is less than 2, return instead of the empty string.'
'Sample String : Python'
'Expected Result : Pyon'
'Sample String : Py'
'Expected Result : PyPy'
'Sample String : w'
'Expected Result : Empty String'

def main():
    char()

def char():
    x = input("Enter a string:")
    if len(x) < 2:
        print("Empty String")
    else:
        print("To get a string made of the first 2 and the last 2 chars :",  (x[0:2] + x[-2:]))

if __name__=="__main__":
    main()