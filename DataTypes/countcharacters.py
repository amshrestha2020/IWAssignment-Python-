'Count the number of characters(character frequency) in a string'
'Sample String: google.com'
'Expected Result: {o:3, g:2, .:1, e:1, l:1, m:1, c:1}'

def CharFrequency(userInput):
    userInput = userInput.lower()
    dict = {}
    for char in userInput:
        keys = dict.keys()
        if char in keys:
            dict[char] += 1
        else:
            dict[char] = 1
    return dict

if __name__ == '__main__':
    userInput = str(input("Enter a string:"))
    print(CharFrequency(userInput))