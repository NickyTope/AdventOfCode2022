
def getCommonChar(str):
    common = []
    idx = 0
    split = len(str) // 2

    a = str[:split]
    b = str[split:]

    for char in a:
        if b.find(char) > -1:
            return char


def getval(char):
    v = ord(char)

    if v > 96: # lower
        return v - 96

    return v - 64 + 26

def getGroupChar(grp):
    a, b, c = grp;

    for char in a:
        if b.find(char) > -1:
            if c.find(char) > -1:
                return char


def part1():
    text = open("day3.txt", "r")
    scores = []
    for line in text:
        char = getCommonChar(line.strip())
        scores.append(getval(char))

    print(scores)
    print(sum(scores))


def part2():
    text = open("day3.txt", "r")
    groups = []
    group = []
    for line in text:
        group.append((line.strip()))
        if len(group) == 3:
            groups.append(group)
            group = []

    scores = []
    for g in groups:
        scores.append(getval(getGroupChar(g)))

    print(scores)
    print(sum(scores))


if __name__ == '__main__':
    # for n in range(97, 97 + 26):
    #     print(getval(chr(n)))
    # for n in range(65, 65 + 26):
    #     print(getval(chr(n)))

    part2()





