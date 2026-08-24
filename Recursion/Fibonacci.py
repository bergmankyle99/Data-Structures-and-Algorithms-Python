def fib(val:int):
    if val <= 1:
        return val
    return fib(val-1) + fib(val-2)

for i in range(7):
    print(fib(i))