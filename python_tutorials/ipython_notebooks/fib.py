import sys
sys.setrecursionlimit(1500)
# Recursive Fib
def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
# print(fib(35))

# Memoization recursive call
fib_memo_dict = {}
def fib_memo(n):
    if n in fib_memo_dict:
        return fib_memo_dict[n]
    if n < 2:
        return_obj = 1
    else:
        return_obj = fib_memo(n-1)+fib_memo(n-2)
    fib_memo_dict[n] = return_obj
    return return_obj
# print(fib_memo(1498))


# Bottom up approach
def fib_bottom(n):
    fib_dict = {}
    for k in range(0,n+1):
        if k <= 2:
            return_obj = 1
        else:
            return_obj = fib_dict[k-1] + fib_dict[k-2]
        fib_dict[k] = return_obj
    return fib_dict[n]
print(fib_bottom(10000))
