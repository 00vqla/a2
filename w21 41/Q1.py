def Unknown(x, y):
    if x < y:
        print(int(x + y))
        return int(Unknown(x + 1, y) * 2)
    else:
        if x == y:
            return 1
        else:
            print(int(x + y))
            return int(Unknown(x - 1, y) // 2)


def IterativeUnknown(x, y):
    total = 1
    while x != y:
        print(x + y)
        if x < y:
            x += 1
            total *= 2
        else:
            x -= 1
            total - int(total / 2)
    return total


print("10 and 15 as input")
print(str(Unknown(10, 15)))
print("both 10 as input")
print(str(Unknown(10, 10)))
print("15 and 10 as input")
print(str(Unknown(15, 10)))

