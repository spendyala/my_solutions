def balance_symbols(string_to_balance_list, max_replacements_list):
    return_obj = []
    for string_to_balance, max_replacements in zip(string_to_balance_list, max_replacements_list):
        temp = string_to_balance
        while '<>' in temp:
            temp = temp.replace('<>', '')
        if not temp:
            return_obj.append(1)
        elif temp[-1] == '<':
            return_obj.append(0)
        elif temp.count('>') <= max_replacements:
            return_obj.append(1)
        else:
            return_obj.append(0)
        # print('String to balance:%s result is "%s".' % (string_to_balance, temp))
    return return_obj

strings_to_balance = ['<<<>>>', '<>>', '<><>', '<<>', '<>>>><<<<>', '<>>>><>']
max_replacements = [10, 0, 0, 0, 0, 5]
print(balance_symbols(strings_to_balance, max_replacements))
