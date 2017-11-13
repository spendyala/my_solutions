def is_edit_distance_1(str1, str2):
    edit_distance_val = edit_distance(str1, str2, len(str1)-1, len(str2)-1)
    print(edit_distance_val, str1, str2)
    if edit_distance_val > 1:
        return False
    return True

def edit_distance(str1, str2, i, j):
    if i < 0 or j < 0:
        return 0
    elif str1[i] == str2[j]:
        return edit_distance(str1, str2, i-1, j-1)
    else:
        return 1 + min(edit_distance(str1, str2, i-1, j),
                       edit_distance(str1, str2, i, j-1),
                       edit_distance(str1, str2, i-1, j-1))

assert is_edit_distance_1('pale', 'ple') == True
assert is_edit_distance_1('palea', 'pale') == True
assert is_edit_distance_1('pale', 'bale') == True
assert is_edit_distance_1('pale', 'bake') == False
assert is_edit_distance_1('pale', 'pale') == True
