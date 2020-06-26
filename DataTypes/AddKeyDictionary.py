'To add a key to a dictionary.'
'Sample Dictionary : {0:10, 1:20}'
'Expected Result: {0:10, 1:20, 2:30}'

def main():
    d = { 0:10, 1:20}
    print("Sample Dictionary as d :", d)

    x = {2:30}
    d.update(x)

    print("Adding a key to a dictionary :", d)

if __name__=="__main__":
    main()
