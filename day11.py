import math


class Monkey:
    def __init__(self, items, operation, test_div_by, test_next):
        self.items = items
        self.operation = operation.split("=")[1].strip().split(" ")
        self.test_div_by = int(test_div_by.split(" ")[2])
        self.test_next = test_next
        self.op_count = 0

    def op(self, item):
        a, operator, b = self.operation
        if a == "old":
            a = item
        else:
            a = int(a)
        if b == "old":
            b = item
        else:
            b = int(b)

        self.op_count += 1

        if operator == "+":
            return a + b
        else:
            return a * b

    def test(self, item):
        # return not math.fmod(item, self.test_div_by) > 0
        return item % self.test_div_by == 0


def game_round(monkeys, easing, factor):
    for monkey in monkeys:
        for item in monkey.items:
            item = monkey.op(item)
            if easing:
                item = round(item / 3)
            if factor is not None:
                item %= factor
            if monkey.test(item):
                monkeys[monkey.test_next[0]].items.append(item)
            else:
                monkeys[monkey.test_next[1]].items.append(item)
        monkey.items = []


def parse_monkeys(in_text):
    monkeys = []
    monkeys_txt = in_text.split("\n\n")
    for monkey_txt in monkeys_txt:
        skipped_id = False
        next_monkey_id = []
        items = []
        operation = ""
        test_div_by = ""
        for line in monkey_txt.split("\n"):
            if not skipped_id:
                skipped_id = True
                continue
            tag, value = line.strip().split(":")
            if tag == "Starting items":
                items = list(map(int, value.strip().split(",")))
            elif tag == "Operation":
                operation = value.strip()
            elif tag == "Test":
                test_div_by = value.strip()
            else:
                next_id = int(value.strip().split(" ")[3])
                next_monkey_id.append(next_id)

        monkeys.append(Monkey(items, operation, test_div_by, next_monkey_id))

    return monkeys


def part1(in_text):

    monkeys = parse_monkeys(in_text)

    for _ in range(20):
        game_round(monkeys, True)

    for monkey in monkeys:
        print(monkey.items)

    op_counts = []
    for monkey in monkeys:
        op_counts.append(monkey.op_count)

    op_counts.sort()
    print(op_counts)
    a = op_counts.pop()
    b = op_counts.pop()

    return a * b


def part2(in_text):

    monkeys = parse_monkeys(in_text)

    # thanks reddit
    factor = math.prod([monkey.test_div_by for monkey in monkeys])

    for _ in range(10000):
        game_round(monkeys, False, factor)

    for monkey in monkeys:
        print(monkey.items)

    op_counts = []
    for monkey in monkeys:
        op_counts.append(monkey.op_count)

    op_counts.sort()
    print(op_counts)
    a = op_counts.pop()
    b = op_counts.pop()

    return a * b


if __name__ == '__main__':
    text = open("day11.txt", "r")
    print(part2(text.read()))
