

def e_contains(e1, e2):
    return e1[0] <= e2[0] and e1[1] >= e2[1]


def e_overlaps(e1, e2):
    l1, u1 = e1
    l2, u2 = e2
    return not (u1 < l2 or u2 < l1)


def part1():
    text = open("day4.txt", "r")
    pairs_found = 0
    for line in text:
        e1, e2 = line.strip().split(",")
        e1 = list(map(int, e1.split("-")))
        e2 = list(map(int, e2.split("-")))
        if e_contains(e1, e2) or e_contains(e2, e1):
            pairs_found += 1

    print(pairs_found)


def part2():
    text = open("day4.txt", "r")
    pairs_found = 0
    for line in text:
        e1, e2 = line.strip().split(",")
        e1 = list(map(int, e1.split("-")))
        e2 = list(map(int, e2.split("-")))
        if e_overlaps(e1, e2):
            pairs_found += 1

    print(pairs_found)


if __name__ == '__main__':
    part1()
    part2()



