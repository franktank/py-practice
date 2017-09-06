# DFS -> return when 0 or invalid boundary
# return size
# At each index that is 1 -> find size

def get_inputs():
    rows = input()
    columns = input()
    matrix = [[None for _ in range(rows)] for _ in range(columns)]
    for i in range(rows):
        for j in range(columns):
            matrix[i][j] = input()

    print(get_largest_region(matrix))

def get_largest_region(matrix):
    max_region = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                region_size = dfs(matrix, i, j)
                max_region = max(max_region, region_size)

    return max_region

def dfs(matrix, row, column):
    """
    Search for connected region
    Returns size of region
    Modifies position to be 0 for visited locations
    """
    # Check for out of bounds
    if row < 0 || row >= len(matrix) || column < 0 || column >= len(matrix[0]):
        return 0
    if matrix[row][column] == 0:
        return 0

    size = 1
    matrix[row][column] = 0

    for i in range(row - 1, row + 2):
        for j in range(column - 1, column + 2):
            if !(i == row && j == column)
            size += dfs(matrix, i, j)

    return size
