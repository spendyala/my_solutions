# Complete the function below.


def printSnakeString():
    input_str='Google Worked'
    print input_str
    str_3 = ''
    str_2 = ''
    str_1 = ''
    counter = 0
    for each in input_str:
        if each == ' ':
            each = '~'
        if (counter % 3) == 1:
            str_3 += each
            str_2 += ' '
            str_1 += ' '
        elif (counter % 3) == 2:
            str_3 += ' '
            str_2 += each
            str_1 += ' '
        elif (counter % 3) == 0:
            str_3 += ' '
            str_2 += ' '
            str_1 += each
        counter += 1
    print str_1
    print str_2
    print str_3

printSnakeString()
