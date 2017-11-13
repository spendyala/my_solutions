import copy
input_str = '??'


def string_per(input_str_list, i):
    if i == len(input_str_list):
        print(''.join([str(x) for x in input_str_list]))
        return
    if input_str_list[i] == '?':
        for each in [1, 2, 3, 4]:
            temp = copy.deepcopy(input_str_list)
            temp[i] = each
            string_per(temp, i)
    else:
        string_per(input_str_list, i + 1)


string_per(list(input_str), 0)
