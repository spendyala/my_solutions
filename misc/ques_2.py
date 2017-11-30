in_list = [12, 34, 45, 9, 9, 8, 90, 4, 3, 6]
print(in_list)
pointer_even = None
pointer_odd = None
index = 0
len_in_list = len(in_list)

while index < len_in_list:
    if pointer_even and pointer_odd:
        if (pointer_odd == len_in_list or
            pointer_even == len_in_list):
            break
        elif pointer_even > pointer_odd and not in_list[pointer_even] & 1:
            even_num = in_list[pointer_even]
            odd_num = in_list[pointer_odd]
            in_list[pointer_even] = odd_num
            in_list[pointer_odd] = even_num
            if pointer_even != pointer_odd:
                pointer_even += 1
                pointer_odd += 1
                index += 1
                continue
    if not in_list[index] & 1:
        pointer_even = index
    elif in_list[index] & 1:
        if pointer_odd is None:
            pointer_odd = index
    index += 1
if not in_list[-1] & 1:
    even_num = in_list[-1]
    odd_num = in_list[pointer_odd]
    in_list[-1] = odd_num
    in_list[pointer_odd] = even_num
print(in_list)
