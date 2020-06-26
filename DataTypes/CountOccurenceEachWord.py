'Program to count the occurences of each word in a given sentence.'

def main():
    count_word()

def count_word():
    h = input("Enter a string :")
    counts = {}
    words = h.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    for i, k in counts.items():
        print(i, k)

if __name__=="__main__":
    main()