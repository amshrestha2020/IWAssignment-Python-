'Find intersection of two given arrays using Lambda'

def ArrayIntersection(A1, A2):
    print("Original arrays:")
    print("A1:", A1)
    print("A2:", A2)

    result = list(filter(lambda i : i in A1, A2)) #using filter method to find new values with lambda function
    print("The intersection of two given arrays as A1 and A2 is:", result)

if __name__ == "__main__":
    A1 = [1, 2, 3, 4, 5]
    A2 = [1, 0, 6, 7, 8, 9, 2]
    ArrayIntersection(A1, A2)
