'Program to remove duplicates from a list'

def main():
    remove_list()

def remove_list():
    before_removing_list = [2, 3, 1, 5, 2, 5, 6, 1, 3, 9]
    print("Before Removing List : {}".format(before_removing_list))

    after_removing_list = []
    for item in before_removing_list:
        if item not in after_removing_list:
            after_removing_list.append(item)
    print("After Removing List: {}".format(after_removing_list))


if __name__=="__main__":
    main()