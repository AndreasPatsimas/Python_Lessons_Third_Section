# same input -> always same output
# no side effects in outside world of function e.g. print() inside a function has a side effect to outside world


# pure function
def multiply_by_two(my_list=None):
    if my_list is None or type(my_list) is not list:
        my_list = []
    new_list = []
    for item in my_list:
        new_list.append(item * 2)
    return new_list


print(multiply_by_two([1, 2, 3]))


# non pure function
def multiply_by_two_non_pure(my_list: list = []):
    new_list = []
    for item in my_list:
        new_list.append(item * 2)
    print(new_list)
    return new_list
