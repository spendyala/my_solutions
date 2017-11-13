print('FUN_1')
def fun_1(n):
    if not n:
        return 0
    print(n)
    return fun_1(n-1)

fun_1(5)


print('FUN_2')
def fun_2(n):
    if n == 100:
        return n
    print(n)
    return fun_2(n+1)

fun_2(0)

print('FUN_3')
def fun_3(n):
    if not n:
        return 0
    print(n)
    val = fun_3(n-1)
    print(n-1)
    return val
fun_3(10)
