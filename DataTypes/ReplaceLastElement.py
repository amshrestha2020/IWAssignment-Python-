'Program to replace the last element in a list with another list.'
'Sample data: [1,3,5,7,9,10],[2,4,6,8]'
'Expected Output: [1,3,5,7,9,2,4,6,8]'

def main():
    sample1 = [1, 3, 5, 7, 9, 10]
    sample2 = [2, 4, 6, 8]
    print("First Sample Data :", sample1)
    print("Second Sample Data :", sample2)

    sample1[-1:] = sample2
    print("Replacing the last element in a list with another list :", sample1)

if __name__=="__main__":
    main()