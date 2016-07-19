# "3 4 5 + *"
# 1. separated by one single space.
# 2. each token must be a number, {+, -, *, /}
# RPN
# "3 4 5 + *" => 3*(4+5) => 27
# "3 4 + 5 *" => (3+4)*5 => 35
# 0.75*5 = 3.75

input_str = "3 4 / 5 *"

def str_to_list(input_str):
    elements_list = []
    for each in input_str.split():
        if each.isdigit():
            elements_list.append(float(each))
        else:
            elements_list.append(each)
    return elements_list


def postfix(input_str):
    elements_list = str_to_list(input_str)
    print elements_list
    stack = []
    for each in elements_list:
        if each in ['+', '-', '*', '/']:
            try:
                var2 = stack.pop()
                var1 = stack.pop()
                val = eval('%f %s %f' % (var1, each, var2))
                stack.append(val)
            except IndexError as index_error:
                print 'Invalid RPN %s' % (input_str, )
                exit(0)
        elif isinstance(each, float):
            stack.append(each)
        else:
            print 'Invalid operator or number'
            exit(0)
    if len(stack) == 1:
        print stack.pop()
    else:
        print 'Invalid RPN %s' % (input_str, )

postfix(input_str)
