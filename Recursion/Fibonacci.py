def fib(val:int):#Time:O(2^n), Space:O(n), space is height of recursive tree
    if val <= 1:
        return val
    return fib(val-1) + fib(val-2)

for i in range(7):
    print(fib(i))