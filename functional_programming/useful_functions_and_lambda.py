from functools import reduce

# lambda param: action(param)


def multiply_by_two(my_list=None):
    if my_list is None or type(my_list) is not list:
        my_list = []
    new_list = []
    for item in my_list:
        new_list.append(item * 2)
    return new_list


def multiply_by_two_func(item):
    return item * 2


def check_odd(item):
    return item % 2 != 0


new_list = list(map(multiply_by_two_func, [1, 2, 3]))
print("new_list", new_list)

new_lambda_list = list(map(lambda param: param*2, [1, 2, 3]))
print("new_lambda_list", new_lambda_list)

new_filtered_list = list(filter(check_odd, [1, 2, 3]))
print("new_filtered_list", new_filtered_list)

new_lambda_filtered_list = list(filter(lambda param: param % 2 != 0, [1, 2, 3]))
print("new_lambda_filtered_list", new_lambda_filtered_list)

teers_list = ["teers", "volun", "tot"]
ziped_list = list(zip(new_list, new_filtered_list, teers_list))
print("ziped_list", ziped_list)


def accumulator(acc, item):
    return acc + item


reduced_value = reduce(accumulator, new_list, 0)
print("reduced_value", reduced_value)


reduced_lambda_value = reduce(lambda acc, param: acc + param, new_list)
print("reduced_lambda_value", reduced_lambda_value)

my_list = [5, 4, 3]

my_list = list(map(lambda param: param * param, my_list))

print(my_list)

a = [(0, 2), (4, 3), (9, 9), (10, -1)]
#sort by second value in every tuple
a.sort(key=lambda param: param[1])
print(a)