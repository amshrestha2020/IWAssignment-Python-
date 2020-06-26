'Program to iterate over dictionaries using for loops.'

d = { 'a' : 1, 'b' : 2, 'c' : 3}
print("Sample data :", d)

def main():
    for x_key, x_value in d.items():
         print(x_key, '->', x_value)

if __name__=="__main__":
    main()