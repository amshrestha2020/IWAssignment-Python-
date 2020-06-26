'Check whether a number is in a given range'

def checkinrange(i):
    if i in range(1, 9):
        print("The number is in a given range:", str(i))
    else:
        print("The number is not in a given range:", str(i))
checkinrange(3)