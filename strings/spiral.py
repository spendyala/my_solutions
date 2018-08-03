

directions = {
    0: (0, 1),  # Go Right
    1: (1, 0),  # Go Down
    2: (0, -1), # Go Left
    3: (-1, 0), # Go Up
}


def should_turn(cur_row, cur_col, rows, cols):
    '''
    Consider these grids to understand what the below code does.
        O O O O O O #
        # O O O O # O
        O # O O # O O
        O # O O O # O
        # O O O O O #
        =
        O O O	 O O O #
        # O O	 O O # O
        O # O	 O # O O

        O # O	 O O # O
        # O O	 O O O #
	< (rows + 1) / 2 will give priority to top part when current position is horizontally
	centered.
	< cols / 2 will give priority to right part when current position is vertically centered.
    '''
    # Check if position is in top-left part.
    print(cur_row, cur_col, rows, cols, 'Current Position')

    if ((cur_row < (rows + 1) / 2) and (cur_col < cols / 2)):
        print(cur_row, (rows + 1) / 2, cur_col, cols / 2, 'Top Left')
        # Condition to turn when current position is in top-left part.
        return cur_row == cur_col + 1
    # Condition to turn when current position in other parts.
    print(cur_row, rows-1-cur_row, min(cur_row, rows-1-cur_row), cur_col, cols-1-cur_col, min(cur_col, cols-1-cur_col), 'Others')
    return min(cur_row, rows-1-cur_row) == min(cur_col, cols-1-cur_col)


def print_spirally(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    total = rows * cols

    # Initial position is at top left corner with direction towards right.
    output = []
    direction = 0
    cur_row = 0
    cur_col = 0

    for idx in range(0, total):
        print('Char:', matrix[cur_row][cur_col])
        output.append(matrix[cur_row][cur_col])
        if should_turn(cur_row, cur_col, rows, cols):
            direction = (direction + 1) % 4
        cur_row += directions[direction][0]
        cur_col += directions[direction][1]
    return ''.join(output)

input_matrix = [
    ['a', 'b', 'c', 'd', 'e'],
    ['f', 'g', 'h', 'i', 'j'],
    ['k', 'l', 'm', 'n', 'o'],
    ['p', 'q', 'r', 's', 't'],
    ['u', 'v', 'w', 'x', 'y'],
    ['z', '0', '1', '2', '3'],
]

input_matrix = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i']
]

input_matrix = [
    ['a', 'b', 'c', 'd'],
    ['e', 'f', 'g', 'h'],
    ['i', 'j', 'k', 'l'],
    ['m', 'n', 'o', 'p']
]

print(print_spirally(input_matrix))
