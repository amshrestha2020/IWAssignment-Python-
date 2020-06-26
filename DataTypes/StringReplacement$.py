'Get a string from a given string where all occurrences of its first char '
'Changes to $ except the first char itself'
'Sample String: restart'
'Expected Result: resta$t'

def main():
    x = input("Enter a string:")
    print("Original String:", x)
    char = x[0]
    x = x.replace(char, '$')
    x = char + x[1:]
    print("Replaced string:", x)

if __name__=="__main__":
    main()
