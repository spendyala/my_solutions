target = '123'

def rec(target, num):
    if len(target) == 1:
        print(num + target[0])
    else:
        for letter in target:
            rec(target.replace(letter, ''), num+letter)

to_print = ''
rec(target, to_print)
