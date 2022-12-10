def part1(in_text):
    cycle = 0
    report_intervals = {20, 60, 100, 140, 180, 220}
    results = []
    x = 1
    for line in in_text.strip().split("\n"):
        if line == "noop":
            cycle += 1
            if cycle in report_intervals:
                results.append(x * cycle)
        else:
            _, amount = line.split(" ")
            cycle += 1
            if cycle in report_intervals:
                results.append(x * cycle)
            cycle += 1
            if cycle in report_intervals:
                results.append(x * cycle)
            x += int(amount)

    print(results)
    return sum(results)


def draw(cycle, x, row, results):
    if x < 2:
        sprite = {0, 1, 2}
    elif x > 37:
        sprite = {37, 38, 39}
    else:
        sprite = {x-1, x, x+1}

    pixel = "."
    if cycle - 1 - (row * 40) in sprite:
        pixel = "#"
    results[row] += pixel

    # print(f"cycle {cycle}")
    # print(f"x {x}")
    # print(results[row])


def part2(in_text):
    cycle = 0
    row = 0
    results = ["", "", "", "", "", ""]
    right_intervals = {40, 80, 120, 160, 200, 240}
    x = 1

    for line in in_text.strip().split("\n"):
        if line == "noop":
            cycle += 1
            draw(cycle, x, row, results)
            if cycle in right_intervals:
                row += 1
        else:
            _, amount = line.split(" ")
            cycle += 1
            draw(cycle, x, row, results)
            if cycle in right_intervals:
                row += 1
            cycle += 1
            draw(cycle, x, row, results)
            if cycle in right_intervals:
                row += 1
            x += int(amount)

    print("DONE")
    for line in results:
        print(line)
    return results


if __name__ == '__main__':
    text = open("day10.txt", "r")
    part2(text.read())