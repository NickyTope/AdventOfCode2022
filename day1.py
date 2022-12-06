def get_elves():
    text = open("day1.txt", "r")
    elves = []
    elf = 0
    for line in text:
        if line == "\n":
            elves.append(elf)
            elf = 0
        else:
            elf += int(line)
    return elves


def part1():
    elves = get_elves()

    highest = 0
    for e in elves:
        if e > highest:
            highest = e

    print(f'highest: {highest}')


def part2():
    elves = get_elves()
    elves.sort()

    one = elves.pop()
    two = elves.pop()
    three = elves.pop()
    total = one + two + three

    print(f'one: {one}, two: {two}, three: {three}, total: {total}')


if __name__ == '__main__':
    part2()