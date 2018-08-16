
operators = {'-', '+', '*', '/'}

def prefix_postfix(input_prefix_exp):
    output_postfix_exp = []
    for each_value in input_prefix_exp[::-1]:
        if each_value in operators:
            val_1 = output_postfix_exp.pop()
            val_2 = output_postfix_exp.pop()
            expression_to_push = f'{val_1}{val_2}{each_value}'
            output_postfix_exp.append(expression_to_push)
        else:
            output_postfix_exp.append(each_value)
    return output_postfix_exp[0]

print(prefix_postfix('*-A/BC-/AKL'))
