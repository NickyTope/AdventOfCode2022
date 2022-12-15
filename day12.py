from collections import deque


row = 0
col = 1


class QueueItem:
    def __init__(self, coord: tuple, distance: int):
        self.coord = coord
        self.distance = distance


def bfs(matrix, start, end):
    next_rows = [-1, 0, 0, 1]
    next_cols = [0, -1, 1, 0]

    max_row = len(matrix)
    max_col = len(matrix[0])
    # print(f"max {max_row} {max_col}")

    visited = [[False for _ in range(max_col)] for _ in range(max_row)]
    visited[start[row]][start[col]] = True

    queue = deque()
    queue.append(QueueItem(start, 0))

    while queue:
        node = queue.popleft()
        node_value = matrix[node.coord[row]][node.coord[col]]
        # print(f"node at {node.coord} with value {node_value} and distance {node.distance}")
        if node.coord[row] == end[row] and node.coord[col] == end[col]:
            return node.distance

        for i in range(4):
            next_row = next_rows[i] + node.coord[row]
            next_col = next_cols[i] + node.coord[col]

            # print(f"looking at {next_row}, {next_col}")
            if (next_row >= 0) and (next_row < max_row):
                if (next_col >= 0) and (next_col < max_col):
                    # print(f"in range, visited: {visited[next_row][next_col]}")
                    if not visited[next_row][next_col]:
                        next_value = matrix[next_row][next_col]
                        # print(f"value {next_value}")
                        if next_value <= node_value + 1:
                            # print("traversable")
                            visited[next_row][next_col] = True
                            next_node = QueueItem((next_row, next_col), node.distance + 1)
                            queue.append(next_node)
    return -1


def part1(in_text):
    matrix = []
    start = None
    end = None
    x = 0
    for line in in_text.strip().split("\n"):
        entry = []
        y = 0
        for char in line:
            if char == "S":
                entry.append(1)
                start = (x, y)
                print(f"start {start}")
            elif char == "E":
                entry.append(27)
                end = (x, y)
                print(f"end {end}")
            else:
                entry.append(ord(char) - 95)
            y += 1
        matrix.append(entry)
        x += 1

    for m in matrix:
        print(m)

    return bfs(matrix, start, end)


def part2(in_text):
    matrix = []
    start = None
    end = None
    x = 0
    for line in in_text.strip().split("\n"):
        entry = []
        y = 0
        for char in line:
            if char == "S":
                entry.append(1)
                start = (x, y)
                print(f"start {start}")
            elif char == "E":
                entry.append(27)
                end = (x, y)
                print(f"end {end}")
            else:
                entry.append(ord(char) - 95)
            y += 1
        matrix.append(entry)
        x += 1

    starting_points = []
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] < 3:
                starting_points.append((row, col))

    scores = []
    for starting_point in starting_points:
        scores.append(bfs(matrix, starting_point, end))

    valid_scores = [score for score in scores if score > 0]

    return min(valid_scores)


if __name__ == '__main__':
    text = open("day12.txt", "r")
    print(part2(text.read()))
