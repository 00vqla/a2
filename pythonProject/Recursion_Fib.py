def fib(n):
    if n <= 0:
        return 0
    elif n == 1:    
        return 1
    else:
        return fib(n-1) + fib(n-2) # rec case


fib_series = [fib(i) for i in range(6)]
print(fib_series)