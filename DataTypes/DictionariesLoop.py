'Program to iterate over dictionaries using Loop'

x = { 'a': 3, 'g': 2, 'h': 6, 'q': 9 }

def main():
    for key, val in x.items():
        print(key, "=", val)

if __name__=="__main__":
    main()