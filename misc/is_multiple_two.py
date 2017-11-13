# 4 = 2^2
# 6 = 10

def is_multiple_two_sol1(number):
    bin_number_length = len(bin(number)[2:])
    if (number - (1 << bin_number_length-1)):
        return False
    return True

assert is_multiple_two_sol1(4) == True
assert is_multiple_two_sol1(6) == False

def is_multiple_two_sol2(number):
    if (number - 1) & number:
        return False
    return True

assert is_multiple_two_sol2(4) == True
assert is_multiple_two_sol2(6) == False
