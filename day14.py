rock = "#"
sand = "o"
x = 0
y = 1


def make_coord(in_str: str):
    return [int(n) for n in in_str.split(",")]


def make_grid(in_text):
    # grid: (x, y) -> rock | sand
    grid = {}
    floor = 0
    for line in in_text.split("\n"):
        coords = list(map(make_coord, line.strip().split(" -> ")))
        for i in range(len(coords)):
            this_coord = coords[i]
            if this_coord[y] > floor:
                floor = this_coord[y]
            if len(coords) > i + 1:
                next_coord = coords[i + 1]
                if this_coord[x] != next_coord[x]:
                    from_x = min(this_coord[x], next_coord[x])
                    to_x = max(this_coord[x], next_coord[x]) + 1
                    grid_y = this_coord[y]
                    for grid_x in range(from_x, to_x):
                        grid[(grid_x, grid_y)] = rock
                if this_coord[y] != next_coord[y]:
                    from_y = min(this_coord[y], next_coord[y])
                    to_y = max(this_coord[y], next_coord[y]) + 1
                    grid_x = this_coord[x]
                    for grid_y in range(from_y, to_y):
                        grid[(grid_x, grid_y)] = rock
    return grid, floor


def settle_sand(grid, floor):
    new_sand = [500, 0]
    while new_sand[y] < floor:
        if (new_sand[x], new_sand[y]+1) not in grid:
            # print(f"down to {new_sand[x]} {new_sand[y]+1}")
            new_sand[y] += 1
        elif (new_sand[x]-1, new_sand[y]+1) not in grid:
            # print(f"down to {new_sand[x]-1} {new_sand[y]+1}")
            new_sand[x] -= 1
            new_sand[y] += 1
        elif (new_sand[x]+1, new_sand[y]+1) not in grid:
            # print(f"down to {new_sand[x]+1} {new_sand[y]+1}")
            new_sand[x] += 1
            new_sand[y] += 1
        else:
            grid[(new_sand[x], new_sand[y])] = sand
            return True
    return False


def settle_sand_to_floor(grid, floor):
    new_sand = [500, 0]
    while new_sand[y] < floor - 1:
        if (new_sand[x], new_sand[y]+1) not in grid:
            # print(f"down to {new_sand[x]} {new_sand[y]+1}")
            new_sand[y] += 1
        elif (new_sand[x]-1, new_sand[y]+1) not in grid:
            # print(f"down to {new_sand[x]-1} {new_sand[y]+1}")
            new_sand[x] -= 1
            new_sand[y] += 1
        elif (new_sand[x]+1, new_sand[y]+1) not in grid:
            # print(f"down to {new_sand[x]+1} {new_sand[y]+1}")
            new_sand[x] += 1
            new_sand[y] += 1
        elif new_sand[y] == 0:
            # couldn't fall
            return False
        else:
            grid[(new_sand[x], new_sand[y])] = sand
            return True
    # settled on floor
    grid[(new_sand[x], new_sand[y])] = sand
    return True


def part1(in_text):
    grid, floor = make_grid(in_text)
    # print(f"floor {floor}")
    sand_count = 0
    exhausted = False
    while not exhausted:
        # print(f"sand {sand_count}")
        if settle_sand(grid, floor):
            sand_count += 1
        else:
            exhausted = True

    return sand_count


def part2(in_text):
    grid, floor = make_grid(in_text)
    # print(f"floor {floor}")
    sand_count = 0
    exhausted = False
    real_floor = floor + 2
    while not exhausted:
        # print(f"sand {sand_count}")
        if settle_sand_to_floor(grid, real_floor):
            sand_count += 1
        else:
            exhausted = True

    # need to place the last piece at the top
    return sand_count + 1


if __name__ == '__main__':
    text = open("day14.txt", "r")
    print(part2(text.read()))
