import re


def read_stack(rawstack):
    lines = rawstack.split("\n")
    dict = {}
    for line in lines:
        i = 0
        stack_idx = 0
        while i < len(line)+1:
            part = line[i:i+4]
            p = re.search("[A-Z]", part)
            if p:
                if stack_idx not in dict:
                    dict[stack_idx] = []
                dict[stack_idx].append(p.group())
            i += 4
            stack_idx += 1
    stacks = []
    i = 0
    while i <= max(dict.keys()):
        dict[i].reverse()
        stacks.append(dict[i])
        i += 1
    return stacks


def part1():
    file = open("day5.txt")
    rawstack, moves = file.read().split("\n\n")
    stacks = read_stack(rawstack)

    for move in moves.split("\n"):
        parts = move.split(" ")
        mcount = int(parts[1])
        mfrom = int(parts[3])
        mto = int(parts[5])

        i = 0
        while i < mcount:
            crate = stacks[mfrom - 1].pop()
            stacks[mto - 1].append(crate)
            i += 1

    answer = ""
    for s in stacks:
        if len(s) > 0:
            answer = answer + s.pop()

    print(answer)


def part2():
    file = open("day5.txt")
    rawstack, moves = file.read().split("\n\n")
    stacks = read_stack(rawstack)

    for move in moves.split("\n"):
        parts = move.split(" ")
        mcount = int(parts[1])
        mfrom = int(parts[3])
        mto = int(parts[5])

        i = 0
        partial = []
        while i < mcount:
            crate = stacks[mfrom - 1].pop()
            partial.append(crate)
            i += 1
        partial.reverse()
        for p in partial:
            stacks[mto - 1].append(p)

    answer = ""
    for s in stacks:
        if len(s) > 0:
            answer = answer + s.pop()

    print(answer)


if __name__ == '__main__':
    part2()