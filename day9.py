vert = 0
horiz = 1


other = {
    vert: horiz,
    horiz: vert,
}


def add(piece, move_dir):
    piece[move_dir] += 1


def minus(piece, move_dir):
    piece[move_dir] -= 1


def has_gap(head, tail, move_dir):
    if head[move_dir] > tail[move_dir]:
        return head[move_dir] - tail[move_dir] > 1
    return tail[move_dir] - head[move_dir] > 1


def part1(in_text):
    history = []
    head = [0, 0]
    tail = [0, 0]
    history.append((tail[vert], tail[horiz]))

    for instruction in in_text.strip().split("\n"):
        direction, num = instruction.split(" ")
        count = int(num)
        if direction == "R" or direction == "L":
            inline = head[vert] == tail[vert]
            move_dir = horiz
        else:
            inline = head[horiz] == tail[horiz]
            move_dir = vert
        if direction == "U" or direction == "R":
            op = add
        else:
            op = minus

        for i in range(count):
            op(head, move_dir)
            if has_gap(head, tail, move_dir):
                op(tail, move_dir)
                if not inline:
                    tail[other[move_dir]] = head[other[move_dir]]
                history.append((tail[vert], tail[horiz]))
            # print(f"move {head} {tail}")

    positions = set(history)
    print(f"moved {len(history)} times over {len(positions)} squares")
    return len(positions)


def is_inline(a, b, move_dir):
    return a[other[move_dir]] == b[other[move_dir]]


def process_move(a, b):
    moved = False

    a_vert, a_horiz = a
    b_vert, b_horiz = b

    vert_gap = a_vert - b_vert
    horiz_gap = a_horiz - b_horiz

    if abs(vert_gap) + abs(horiz_gap) > 2:
        # print(f"diagonal {vert_gap} {horiz_gap}")
        # move diagonal
        if vert_gap > 0:
            b[vert] += 1
        else:
            b[vert] -= 1
        if horiz_gap > 0:
            b[horiz] += 1
        else:
            b[horiz] -= 1
        return True

    if a_horiz > b_horiz and a_horiz - b_horiz > 1:
        b[horiz] += 1
        moved = True
    elif b_horiz > a_horiz and b_horiz - a_horiz > 1:
        b[horiz] -= 1
        moved = True

    if a_vert > b_vert and a_vert - b_vert > 1:
        b[vert] += 1
        moved = True
    elif b_vert > a_vert and b_vert - a_vert > 1:
        b[vert] -= 1
        moved = True

    return moved

def part2(in_text):
    history = []
    head = [0, 0]
    tail = [0, 0]
    rope = [
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        tail,
    ]
    history.append((tail[vert], tail[horiz]))

    for instruction in in_text.strip().split("\n"):
        direction, num = instruction.split(" ")
        count = int(num)
        if direction == "R" or direction == "L":
            move_dir = horiz
        else:
            move_dir = vert
        if direction == "U" or direction == "R":
            op = add
        else:
            op = minus

        for moves in range(count):
            op(head, move_dir)
            last = head
            for i in range(len(rope)):
                # print(f"before {last} {rope[i]}")
                moved = process_move(last, rope[i])
                # print(f"after  {last} {rope[i]}")
                if rope[i] is tail and moved:
                    history.append((tail[vert], tail[horiz]))
                last = rope[i]
            # print(f"move {head} {rope}")

    positions = set(history)
    print(f"moved {len(history)} times over {len(positions)} squares")
    return len(positions)


if __name__ == '__main__':
    text = open("day9.txt", "r")
    print(part2(text.read()))