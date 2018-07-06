def get_unique_number(input_str):
    if not input_str:
        return 0
    # assign each character a unique number
    char_to_prime = {
        'a': 2,
        'b': 3,
        'c': 5,
        'd': 7,
        'e': 11,
        'f': 13
    }
    output_number = 1
    for each in input_str:
        output_number *= char_to_prime[each]
    return output_number

input_str = 'aaa'
print(input_str, get_unique_number(input_str))
input_str = 'abc'
print(input_str, get_unique_number(input_str))
input_str = 'abcded'
print(input_str, get_unique_number(input_str))


