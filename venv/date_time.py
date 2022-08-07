import datetime
import pdb # pythοn debugger

print(datetime.time(10, 17, 3))
print(datetime.date.today())

def add(num1, num2):
    pdb.set_trace() # useful commands -> help, step, continue, a ,run
    return num1 + num2

add(1, "dsf")