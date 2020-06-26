'Program to count the number of strings where the string length is 2 or more'
'the first and last character are same from a given list of strings'
'Sample List:[abc, xyz, aba, 1221]'
'Expected Result: 2'

def main():
    r = input("Enter a list(space separated)=")
    t = list(r.split())
    c = 0
    for word in t:
        if len(word) > 1 and word[0] == word[-1]:
            c += 1
    print("Count the number of strings from a given list:", c)

if __name__=="__main__":
    main()
