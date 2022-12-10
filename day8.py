#https://stackoverflow.com/questions/53250821/in-python-how-do-i-rotate-a-matrix-90-degrees-counterclockwise
def rotate_matrix(m):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0])-1,-1,-1)]


def update_visible(lst, values):
    i = 0
    n = -1
    for tree in lst:
        if tree > n:
            n = tree
            values[i] = True
        i += 1


def get_visible(lst, values=None):
    if values is None:
        values = []
        for tree in lst:
            values.append(False)
    update_visible(lst, values)
    lst.reverse()
    values.reverse()
    update_visible(lst, values)
    values.reverse()
    lst.reverse()
    return values

def part1(in_text):
    lists = []

    for line in in_text.strip().split("\n"):
        lst = []
        i = 0
        for char in line:
            n = int(char)
            lst.append(n)
        lists.append(lst)

    matrix = []
    for lst in lists:
        matrix.append(get_visible(lst))
    lists = rotate_matrix(lists)
    matrix = rotate_matrix(matrix)
    for i in range(len(lists)):
        update_visible(lists[i], matrix[i])
        lists[i].reverse()
        matrix[i].reverse()
        update_visible(lists[i], matrix[i])
    total = 0
    for row in matrix:
        for cell in row:
            if cell:
                total += 1

    return total


def calc_scene_score(row, col, matrix):
    if row == 0 or col == 0 or row == len(matrix)-1 or col == len(matrix[row])-1:
        return 0

    height = matrix[row][col]
    count = 0
    # left
    ldone = False
    lcount = 0
    i = col - 1
    while i >= 0 and not ldone:
        if matrix[row][i] >= height:
            ldone = True
        lcount += 1
        i -= 1
    # right
    rdone = False
    rcount = 0
    i = col + 1
    while i <= len(matrix[row]) - 1 and not rdone:
        if matrix[row][i] >= height:
            rdone = True
        rcount += 1
        i += 1
    # up
    tdone = False
    tcount = 0
    i = row - 1
    while i >= 0 and not tdone:
        if matrix[i][col] >= height:
            tdone = True
        tcount += 1
        i -= 1
    # down
    ddone = False
    dcount = 0
    i = row + 1
    while i <= len(matrix) - 1 and not ddone:
        if matrix[i][col] >= height:
            ddone = True
        dcount += 1
        i += 1
    return lcount * rcount * tcount * dcount


def part2(in_text):
    matrix = []

    for line in in_text.strip().split("\n"):
        row = []
        i = 0
        for char in line:
            n = int(char)
            row.append(n)
        matrix.append(row)

    max = 0
    for row in range(len(matrix)-1):
        for col in range(len(matrix[row])-1):
            score = calc_scene_score(row, col, matrix)
            if score > max:
                max = score

    return max






if __name__ == '__main__':
    text = open("day8.txt", "r")
    print(part2(text.read()))