def is_substring(str_1, str_2):
    if str_2 in str_1:
        return True
    return False

def is_string_rotate(str_1, str_2):
    str_1 += str_1
    if is_substring(str_1, str_2):
        return True
    return False

assert is_string_rotate('abcdef', 'defabc') == True
assert is_string_rotate('abcdefg', 'defabc') == False
assert is_string_rotate('waterbottle', 'tlewaterbot') == True
