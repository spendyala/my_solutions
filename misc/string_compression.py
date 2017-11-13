def string_compression(input_str):
    compressed_list = []
    previous = None
    count = 0

    for each_char in input_str:
        if not previous:
            count += 1
            previous = each_char
        elif previous == each_char:
            count += 1
        else:
            compressed_list.append(previous)
            compressed_list.append(str(count))
            count = 1
            previous = each_char
    compressed_list.append(previous)
    compressed_list.append(str(count))
    compressed_str = ''.join(compressed_list)
    if len(compressed_str) == len(input_str):
        return input_str
    return compressed_str

assert string_compression('aabcccccaaa') == 'a2b1c5a3'
assert string_compression('aabbccaa') == 'aabbccaa'
