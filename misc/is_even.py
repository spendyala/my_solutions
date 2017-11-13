def is_even_pow(number):
    if number & (number-1):
        return False
    return True

assert is_even_pow(5) == False
assert is_even_pow(8) == True
assert is_even_pow(16) == True
assert is_even_pow(12) == False
