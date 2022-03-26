count = 0

def inputInteger(prompt):
    n = int(input(prompt))
    return n

def test():
    global count
    a = inputInteger("Enter a number: ")

    if a % 2 == 0:
        print("Even")
    else:
        print("Odd")

    print("Ternary: Even" if a % 2 == 0 else "Ternary: Odd")

    print("count: {}".format(count))
    if count < 3:
        count += 1
        test()

test()

