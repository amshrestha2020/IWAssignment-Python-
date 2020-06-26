'Accepts a string and calculate the number of upper case letters and lower case letters'

class Count:
    def __init__(self, string):
        self.string = string

    def get_count_upper(self):
        count = 0
        for char in self.string:
            if char.isupper():
                count += 1
        return count

    def get_count_lower(self):
        count = 0
        for char in self.string:
            if char.islower():
                count += 1
        return count

if __name__ == "__main__":
    string = input("Enter a string to calculate the upper and lower case letters:")
    obj = Count(string)
    count_upper = obj.get_count_upper()
    count_lower = obj.get_count_lower()
    print("Number of Uppercase characters:", count_upper)
    print("Number of Lowercase characters:", count_lower)

