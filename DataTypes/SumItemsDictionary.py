'Program to sum all the items in a dictionary.'

def main():
    data = { 'iphoneSE' : 300, 'iphone11' : 800, 'ipad' : 400}
    print("Sample data to sum all the items in a dictionary :", data)

    print("The sum of all the sample data :", sum(data.values()))

if __name__=="__main__":
    main()
