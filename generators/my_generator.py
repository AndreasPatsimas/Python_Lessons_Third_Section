# range for example is a generator

def generator_function(num):
    for i in range(num):
        yield i


# for item in generator_function(1000):
#     print(item)

g = generator_function(100)
print(g)

print(next(g))
print(next(g))

#generator faster than looping a simple list