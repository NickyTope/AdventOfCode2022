import re
from itertools import pairwise


class Position:
    def __init__(self, col, row):
        self.col = col
        self.row = row

    def val(self):
        return self.col, self.row

    def distance_to(self, target):
        col_diff = max(self.col, target.col) - min(self.col, target.col)
        row_diff = max(self.row, target.row) - min(self.row, target.row)
        return col_diff + row_diff

    def same(self, target):
        return self.col == target.col and self.row == target.row

    def adjust_col(self, amount: int):
        self.col += amount


class Sensor:
    def __init__(self, position: Position, beacon: Position):
        self.position = position
        self.beacon = beacon
        self.range = position.distance_to(beacon)

    def can_see_row(self, row):
        s_row = self.position.row
        s_range = self.range
        return s_row - s_range <= row <= s_row + s_range

    def empty_in_row(self, row):
        if not self.can_see_row(row):
            return None
        if self.beacon.same(Position(self.position.col, row)):
            return None

        s_col = self.position.col
        s_row = self.position.row
        offset = abs(row - s_row)
        diff = self.range - offset
        start = Position(s_col - diff, row)
        end = Position(s_col + diff, row)
        if self.beacon.row == row:
            if start.same(self.beacon):
                start.adjust_col(1)
            elif end.same(self.beacon):
                end.adjust_col(-1)
        return Range(start.col, end.col)


class Range:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __str__(self):
        return f"{self.start}, {self.end}"

    def overlaps(self, r):
        return self.start <= r.start <= self.end or r.start <= self.start <= r.end

    def contains(self, r):
        return self.start <= r.start and self.end >= r.end

    def has_gap(self, r):
        return self.start > r.end or self.end < r.start


line_regex = "Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)"
def parse_into_sensors(in_text):
    sensors = []
    beacons = set()
    parsed = re.findall(line_regex, in_text)
    for (a, b, c, d) in parsed:
        beacon = Position(int(c), int(d))
        sensors.append(Sensor(Position(int(a), int(b)), beacon))
        beacons.add(beacon.val())
    return sensors, beacons


def get_processed_row_data(sensors, row):
    row_data = []
    for sensor in sensors:
        bounds = sensor.empty_in_row(row)
        if bounds:
            row_data.append(bounds)
    sorted_data = sorted(row_data, key=lambda r: r.start)
    processed = []
    current = None
    for r in sorted_data:
        if not current:
            current = r
            continue
        if current.has_gap(r):
            # print("gap")
            processed.append(current)
            current = r
        else:
            current = Range(min(current.start, r.start), max(current.end, r.end))
    if current:
        processed.append(current)
    return processed


def part1(in_text, target_row):
    sensors, _ = parse_into_sensors(in_text)
    processed = get_processed_row_data(sensors, target_row)
    in_row = 0
    for r in processed:
        in_row += r.end - r.start + 1
    return in_row


def part2(in_text, max_row):
    sensors, beacons = parse_into_sensors(in_text)
    # for sensor in sensors:
    #     print(sensor.position.val(), sensor.range)
    found = None
    row = 0
    while found is None and row <= max_row:
        processed = get_processed_row_data(sensors, row)
        # print(row, processed)
        if len(processed) == 0:
            row += 1
            continue
        if len(processed) > 1:
            for a, b in pairwise(processed):
                if found is None:
                    for i in range(a.end + 1, b.start):
                        if (i, row) not in beacons:
                            found = (i, row)
                            break
        else:
            start, end = processed[0].start, processed[0].end
            if start > 0:
                for i in range(0, start):
                    if (i, row) not in beacons:
                        found = (i, row)
                        break
            if end < max_row:
                for i in range(end + 1, max_row + 1):
                    if (i, row) not in beacons:
                        found = (i, row)
                        break
        row += 1

    if found is None:
        return 0

    return (found[0]*4000000)+found[1]


if __name__ == '__main__':
    text = open("day15.txt", "r").read()
    print(" -- PART ONE --")
    print(part1(text, 2000000))
    print(" -- PART TWO --")
    print(part2(text, 4000000))
