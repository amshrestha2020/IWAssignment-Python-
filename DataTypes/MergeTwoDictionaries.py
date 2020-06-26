'Program to merge two dictionaries'

def mergeDictionaries(d1, d2):
    d3 = { **d1, **d2}
    for key, value in d3.items():
        if key in d1 and key in d2:
            d3[key] = [value, d1[key]]
    return d3

def main():
    'Create first dictionary'
    d1 = { 'Ram' : 1, 'Sam' : 3}
    'Create second dictionary'
    d2 = { 'Hari' : 4}

    print('First Dictionary :')
    print(d1)
    print('Second Dictionary :')
    print(d2)

    print(' Merge Two dictionaries ')
    d1.update(d2)
    print('Updated dictionary')
    print(d1)

if __name__=="__main__":
    main()
