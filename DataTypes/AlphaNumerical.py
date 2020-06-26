'Program that accepts a comma separated sequence of words as input'
'Prints the unique words in sorted form(alphanumerically)'
'Sample Words: red, white, black, red, green, black'
'Expected Words: black, green, red, white, red'

def main():
    items = input("Enter comma separated sequence of words=")
    words = items.split(",")
    for i in words:
        x = (",".join(sorted(list(set(words)))))
    print(x)

if __name__=="__main__":
    main()