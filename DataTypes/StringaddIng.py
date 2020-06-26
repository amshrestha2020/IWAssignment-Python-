'Program to add ing at the end of a given string(length should be at least 3)'
'if the given string already ends with ing then add ly instead.'
'if the string length of the given string is less than 3, leave it unchanged'
'Sample String: abc'
'Expected Result: abcing'
'Sample String: string'
'Expected Result: stringly'

def main():
    a = input("Enter a string:")
    length = len(a)
    if length > 2 :
        if a[-3:] == 'ing':
            a += 'ly'
        else:
            a += 'ing'
    print("New string:", a)

if __name__=="__main__":
    main()