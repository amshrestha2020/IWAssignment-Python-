'Program to remove the characters which have odd index values of a given string.'

def main():
    odd_index()

def odd_index():
    t = input("Enter a string :")
    result = ""
    for i in range(0, len(t), 2):
        if i % 2 == 0:
            result = result + t[i]
    print("Remove the characters which have odd index values :", result)

if __name__=="__main__":
    main()
