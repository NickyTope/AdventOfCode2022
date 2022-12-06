

def bucket_has_dup(b):
    s = set(b)
    return len(b) != len(s)


def part1():
    file = open("day6.txt")
    stream = file.read().strip()
    bucket_size = 4

    bucket = stream[0:bucket_size]
    marker_end = 4
    if not bucket_has_dup(bucket):
        return marker_end

    for char in stream[bucket_size:]:
        marker_end += 1
        bucket = bucket[1:bucket_size] + char
        if not bucket_has_dup(bucket):
            return marker_end


def part2():
    file = open("day6.txt")
    stream = file.read().strip()
    bucket_size = 14

    bucket = stream[0:bucket_size]
    marker_end = 14
    if not bucket_has_dup(bucket):
        return marker_end

    for char in stream[bucket_size:]:
        marker_end += 1
        bucket = bucket[1:bucket_size] + char
        if not bucket_has_dup(bucket):
            return marker_end






if __name__ == '__main__':
    print(part2())