'To concatenate the following dictionaries to create anew oe'
'Sample Dictionary:'
'dic1 = { 1: 10, 2 : 20}'
'dic2 = { 3: 30, 4: 40 }'
'dic3 = { 5: 50, 6: 60}'
'Expected Result : {1:10, 2:20, 3:30, 4:40, 5:50, 6:60}'

def main():
    dic1 = { 1:10, 2:20 }
    dic2 = { 3:30, 4:40 }
    dic3 = { 5:50, 6:60 }
    print("Sample dictionary as dic1 :", dic1)
    print("Sample dictionary as dic2 :", dic2)
    print("Sample dictionary as dic3 :", dic3)
    dic4 = {}

    for x in (dic1, dic2, dic3):
        dic4.update(x)
    print("Expected output :", dic4)

if __name__=="__main__":
    main()