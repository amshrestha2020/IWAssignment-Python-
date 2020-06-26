'Reverse a string'

class Reverse:
    def __init__(self, string):
        self.string = string

    def get_reverse(self):
        rev_string = ""
        for i in range(len(self.string), 0, -1):
            rev_string += self.string[i-1]
        return rev_string

def main():
    string = input("Enter a string:")
    obj = Reverse(string)
    rev_string = obj.get_reverse()
    print("Reversed String:", rev_string)

if __name__ == "__main__":
    main()
