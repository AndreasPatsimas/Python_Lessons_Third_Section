def buy(*args, **kwargs):
    cart = []
    length = len(list(args))
    print(length)
    for item in range(length):
        cart.append(args[item])
    return cart