from pprint import pprint

def rotate_matrix(matrix):
    N = len(a)
    for y in range(0, N//2):
        for x in range(0, N):
            import pdb; pdb.set_trace()
            temp = matrix[x][y]
            matrix[x][y] = matrix[y][N-(x+1)]
            matrix[y][N-(x+1)] = matrix[N-(y+1)][N-(x+1)]
            matrix[N-(y+1)][N-(x+1)] = matrix[N-(y+1)][x]
            matrix[N-(y+1)][x] = temp
    pprint(matrix)

# Correct one
def rotate_matrix_list(matrix):
    N = len(a)
    rotations = N+1 if N%2 else N
    for x in range(0, rotations//2):
        for y in range(x, N-x-1):
            temp = matrix[x][y]
            matrix[x][y] = matrix[N-(y+1)][x]
            matrix[N-(y+1)][x] = matrix[N-(x+1)][N-(y+1)]
            matrix[N-(x+1)][N-(y+1)] = matrix[y][N-(x+1)]
            matrix[y][N-(x+1)] = temp
    pprint(matrix)

a = [[0, 0, 0, 0, 0],
     [1, 1, 1, 1, 1],
     [2, 2, 2, 2, 2],
     [3, 3, 3, 3, 3],
     [4, 4, 4, 4, 4]]
pprint(a)
rotate_matrix_list(a)

a = [[0, 0, 0, 0],
     [1, 1, 1, 1],
     [2, 2, 2, 2],
     [3, 3, 3, 3]]
pprint(a)
rotate_matrix_list(a)
