def factorial(n):
    if n == 1:
        print(n)
        return 1  # base case
    else:
        print(n, '*', end=' ')
        return n * factorial(n - 1)  # Recursive case


print('factorial of 5=', factorial(5))