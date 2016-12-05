# Solution 1
def is_permutation_of_palindrome_sol1(string):
    freq_list = build_char_freq_list(string.replace(' ', ''))
    return check_max_one_odd(freq_list)


def check_max_one_odd(freq_list):
    found_odd = False
    for each_int in freq_list:
        if each_int % 2 == 1:
            if found_odd:
                return False
            found_odd = True
    return True


def build_char_freq_list(string):
    freq_list = [0 for x in range(ord('z')-ord('a')+1)]
    for each_char in string:
        freq_list[ord(each_char)-ord('a')] += 1
    return freq_list

assert is_permutation_of_palindrome_sol1('tact coa') == True
assert is_permutation_of_palindrome_sol1('tact coabbbccc') == False


# Solution 2
def is_permutation_of_palindrome_sol2(string):
    string = string.replace(' ', '')
    count_odd = 0
    freq_list = [0 for x in range(ord('z')-ord('a')+1)]
    for each_char in string:
        freq_index  =ord(each_char)-ord('a')
        freq_list[freq_index] += 1
        if freq_list[freq_index] % 2 == 1:
            count_odd += 1
        else:
            count_odd -= 1
    return count_odd <= 1

assert is_permutation_of_palindrome_sol2('tact coa') == True
assert is_permutation_of_palindrome_sol2('tact coabbbccc') == False


def is_permutation_of_palindrome_sol3(string):
