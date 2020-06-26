'function that takes a list of words and returns the length of the longest one'

def main():
    j = input("Enter a list with strings (space separated):")
    y = j.split()
    length = []
    for n in y:
        length.append((len(n), n))
        print(length)
        length.sort()
        print(length)
    print("Longest length of word:", length[-1][1])

if __name__=="__main__":
    main()