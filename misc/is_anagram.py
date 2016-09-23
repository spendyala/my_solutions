def anagram_sol1(str_1, str_2):  # 3 O(n) + 2O(n log n)
    # If string lenghts are not matching then it is invalid
    # To find lenght of str_1 is O(n) if str_1 has n characters
    # To find lenght of str_2 is O(m) if str_2 has m characters
    if len(str_1) != len(str_2):
        return False

    # Assuming using Quick Sort Best case O(n log n)
    str_1_sorted = sorted(str_1)
    str_2_sorted = sorted(str_2)

    match_flag = True
    index = 0
    while index < len(str_1) and match_flag:  # O(n)
        if str_1_sorted[index] == str_2_sorted[index]:
            index += 1
        else:
            match_flag = False

    return match_flag


def anagram_sol2(str_1, str_2):  # 7 O(n)
    # If string lenghts are not matching then it is invalid
    # To find lenght of str_1 is O(n) if str_1 has n characters
    # To find lenght of str_2 is O(m) if str_2 has m characters
    if len(str_1) != len(str_2):
        return False

    # In this I will assume all the strings are in lower case and ASCII Chars
    N_CHAR = 26
    counters_1 = [0] * N_CHAR  # O(n)
    counters_2 = [0] * N_CHAR  # O(n)

    for each_char in str_1:  # O(n)
        index = ord(each_char) - ord('a')
        counters_1[index] += 1

    for each_char in str_2:  # O(n)
        index = ord(each_char) - ord('a')
        counters_2[index] += 1

    match_flag = True
    index = 0
    while index < N_CHAR and match_flag:  # O(n)
        if counters_1[index] == counters_2[index]:
            index += 1
        else:
            match_flag = False

    return match_flag


# TODO: 3rd solution using prime numbers.


assert anagram_sol1('abcd', 'dbca') == True
assert anagram_sol1('abcd', 'adbca') == False
assert anagram_sol1('abcd', 'adca') == False

assert anagram_sol2('abcd', 'dbca') == True
assert anagram_sol2('abcd', 'adbca') == False
assert anagram_sol2('abcd', 'adca') == False
