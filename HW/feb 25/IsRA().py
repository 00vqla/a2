def isRA(a, b, c):

    if a ^ 2 == b ^ 2 + c ^ 2 or b ^ 2 == a ^ 2 + c ^ 2 or c ^ 2 == a ^ 2 + b ^ 2:
        print("The triangle is right-angled")
    else:
        print("Not a right-angled triangle")


isRA(3, 4, 5)
