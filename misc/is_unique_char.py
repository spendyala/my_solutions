
# assuming ASCII Code and they are 256 characters
# TODO: Notes to read
# https://en.wikipedia.org/wiki/Plane_%28Unicode%29
# http://www.ascii-code.com/
N_COUNT = 256


def is_unique_char(input_str):

    bits_number = 0  # This is extra space
    if len(input_str) > N_COUNT:
        return False

    # Time complexity defined here O(n) where n is lenght of input_str
    for each in input_str:
        # Bit wise operations are single clock cycle
        if bits_number >> ord(each) & 1:
            return False
        bits_number = bits_number | 1 << ord(each)
    return True

assert is_unique_char('abc') == True
assert is_unique_char('abca') == False

test_str = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
assert is_unique_char(test_str) == True
test_str = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZa'
assert is_unique_char(test_str) == False
