import functools
import json

equal = 0
ordered = -1
unordered = 1


def parse_line(input):
    return json.loads(input)


def parse_into_pair(input):
    [left, right] = input.split("\n")
    return parse_line(left), parse_line(right)


def pair_in_order(left, right):
    i = 0
    left_last = len(left) - 1
    right_last = len(right) - 1
    print(f"comparing {left} to {right}")
    if left_last < 0 and right_last < 0:
        return equal
    while True:
        print(f"iter {i} on {left} and {right} with lasts {left_last} and {right_last}")
        if left_last < i <= right_last:
            print(f"exhausted left {left_last} < {i} <= {right_last}")
            return ordered
        elif right_last < i <= left_last:
            print(f"exhausted right {right_last} < {i} <= {left_last}")
            return unordered

        # both exhausted
        if left_last < i and right_last < i:
            return equal

        l = left[i]
        r = right[i]
        # print(f"comparing, {l} and {r}")

        if type(l) is list:
            sub_pair = pair_in_order(l, r) if type(r) is list else pair_in_order(l, [r])
            if sub_pair != equal:
                return sub_pair
        elif type(r) is list:
            sub_pair = pair_in_order(l, r) if type(l) is list else pair_in_order([l], r)
            if sub_pair != equal:
                return sub_pair
        elif r != l:
            # print(f"returning diff {left[i] < right[i]}")
            return ordered if left[i] < right[i] else unordered
        elif i == left_last == right_last:
            # print("equal")
            return equal
        i += 1


def part1(in_text):

    pairs = in_text.split("\n\n")

    i = 1
    in_order = []
    for pair in pairs:
        left, right = parse_into_pair(pair)
        if pair_in_order(left, right) == ordered:
            in_order.append(i)
        i += 1
    print(in_order)

    return sum(in_order)


def part2(in_text):

    pairs = in_text.split("\n\n")
    packets = [
        [[2]],
        [[6]]
    ]
    for pair in pairs:
        left, right = parse_into_pair(pair)
        packets.append(left)
        packets.append(right)

    sorted_packets = sorted(packets, key=functools.cmp_to_key(pair_in_order))

    indexes = []
    for i in range(len(sorted_packets)):
        if sorted_packets[i] == [[2]] or sorted_packets[i] == [[6]]:
            indexes.append(i + 1)

    return indexes[0] * indexes[1]


if __name__ == '__main__':
    text = open("day13.txt", "r")
    print(part2(text.read()))