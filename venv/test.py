#import utility
#import shopping.my_cart
from shopping.my_cart import buy
from utility import sum, Car
#import random # build in module
import random as ap

#suma = utility.sum

print(sum(5, 4))

#my_car = utility.Car("Ford", "black")
my_car = Car("Ford", "black")
print(my_car)

#buy = shopping.my_cart.buy

cart = buy("car", "bike", my_car.__str__())
print(cart)

print(__name__)

#help(random)

# print(random.randint(1, 10))
# print(random.choice(["aris", "naos", "patsiman"]))

print(ap.randint(1, 10))
print(ap.choice(["aris", "naos", "patsiman"]))