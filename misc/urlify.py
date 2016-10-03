# URLify


# To use the same string space.
def urlify(str_to_urlify, true_length):
    spaces_counter = 0
    for each_char in str_to_urlify[:true_length]:
        if each_char == ' ':
            spaces_counter += 1

    index = true_length + spaces_counter * 2
    urlify_str = [' '] * index
    if true_length < len(str_to_urlify):
        urlify_str[true_length] = '\0'

    for str_index in range(true_length-1, -1, -1):
        if str_to_urlify[str_index] == ' ':
            urlify_str[index-1] = '0'
            urlify_str[index-2] = '2'
            urlify_str[index-3] = '%'
            index -= 3
        else:
            urlify_str[index-1] = str_to_urlify[str_index]
            index -= 1
    return ''.join(urlify_str)


def urlify_2(str_to_urlify, true_length):
    spaces_counter = 0
    for each_char in str_to_urlify[:true_length]:
        if each_char == ' ':
            spaces_counter += 1

    index = true_length + spaces_counter * 2
    urlify_str = ''

    for str_index in range(true_length-1, -1, -1):
        if str_to_urlify[str_index] == ' ':
            urlify_str = '%20' + urlify_str
            index -= 3
        else:
            urlify_str = str_to_urlify[str_index] + urlify_str
            index -= 1
    return urlify_str


assert urlify('Mr John Smith    ', 13) == 'Mr%20John%20Smith'
assert urlify_2('Mr John Smith    ', 13) == 'Mr%20John%20Smith'
