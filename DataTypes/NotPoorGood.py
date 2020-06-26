'Program to find the first appearance of the substring not and poor from a given string.'
'if not follows the poor, replace the whole not...poor substring with good'
'Sample String: The lyrics is not that poor!'
'The lyrics is poor!'
'Expected Result: The lyrics is good!'
'The lyrics is poor'

def main():
    sentence = input("Enter a string:")
    a = sentence.find('not')
    b = sentence.find('poor')
    if b > a:
        sentence = sentence.replace(sentence[a:(b+4)], 'good')
    print("Changing the appearance of not..poor :", sentence)

if __name__=="__main__":
    main()