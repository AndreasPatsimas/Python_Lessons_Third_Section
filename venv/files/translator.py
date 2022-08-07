from translate import Translator
#before import python translate install pip3 install translate in cmd
#if error then install microsoft c++ build tools

try:
    with open("C:/Directory1/test.txt", mode="r") as my_file:
        #text = my_file.write(":)")
        print(my_file.read())
except FileNotFoundError as err:
    raise err
