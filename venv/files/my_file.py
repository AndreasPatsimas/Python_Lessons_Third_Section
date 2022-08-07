# my_file = open("C:/Directory1/test.txt")
# #print(my_file.read())
# print(my_file.readline())
# print(my_file.readline())
#
# my_file.close()

with open("C:/Directory1/test.txt", mode="r") as my_file:
    print(my_file.readlines())

# with open("C:/Directory1/test.txt", mode="r+") as my_file:
#     text = my_file.write("yo")
#     print(text)

with open("C:/Directory1/test.txt", mode="a") as my_file:
    text = my_file.write(":)")
    print(text)

try:
    with open("C:/Directory1/tes.txt", mode="r") as my_file:
        text = my_file.write("απ")
        print(text)
except FileNotFoundError as err:
    print("File not found")
    raise err