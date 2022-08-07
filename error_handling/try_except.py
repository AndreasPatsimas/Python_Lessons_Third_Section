while True:
    try:
        age = int(input("what is your age?"))

    except:
        print("Please enter a number")

    else:
        print(age)
        print("thank you")
        break