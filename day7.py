def parse_line(line):
    parts = line.strip().split(" ")
    if parts[0] == "$":
        result = {
            "type": "cmd",
            "command": parts[1]
        }
        if len(parts) > 2:
            result["arg"] = parts[2]
        return result
    elif parts[0] == "dir":
        return {
            "type": "dir",
            "path": parts[1]
        }
    else:
        return {
            "type": "file",
            "path": parts[1],
            "size": int(parts[0])
        }


def get_tree(lines):
    tree = {}
    ptr_stack = [tree]
    path = ""
    for line in lines:
        ptr = ptr_stack[len(ptr_stack) - 1]
        if line["type"] == "cmd":
            if line["command"] == "cd":
                path = line["arg"]
                if path == "..":
                    ptr_stack.pop()
                else:
                    ptr[path] = {
                        "size": 0,
                        "path": path
                    }
                    ptr_stack.append(ptr[path])
        elif line["type"] == "file":
            ptr["size"] += line["size"]

    return tree


def get_totals(branch):
    total = 0
    for key, val in branch.items():
        if key == "size":
            total += val
        elif key != "path":
            total += get_totals(val)
    if "size" in branch:
        branch["total"] = total
    return total


def get_dirs_lt(branch, dirs=None):
    if dirs is None:
        dirs = []
    limit = 100000
    for key, val in branch.items():
        if key != "size" and key != "path" and key != "total":
            if "total" in val and val["total"] <= limit:
                dirs.append((val["path"], val["total"]))
            get_dirs_lt(val, dirs)
    return dirs


def get_dirs(branch, dirs=None):
    if dirs is None:
        dirs = []
    for key, val in branch.items():
        if key != "size" and key != "path" and key != "total":
            if "total" in val:
                dirs.append((val["path"], val["total"]))
            get_dirs(val, dirs)
    return dirs
def part1():
    text = open("day7.txt", "r")
    parsed = []
    for line in text:
        parsed.append(parse_line(line))

    tree = get_tree(parsed)
    print(tree)

    get_totals(tree)
    print(tree)

    dirs = get_dirs_lt(tree)
    print(dirs)

    total = 0
    for path, sub in dirs:
        total += sub

    print(total)


def part2():
    text = open("day7.txt", "r")
    parsed = []
    for line in text:
        parsed.append(parse_line(line))

    tree = get_tree(parsed)
    print(tree)

    get_totals(tree)
    print(tree)

    dirs = get_dirs(tree)
    dirs.sort(key=lambda d: d[1])
    print(dirs)

    total_used = tree["/"]["total"]
    total_avail = 70000000
    remaining = total_avail - total_used
    print(f"total used: {total_used}, remaining: {remaining}")

    target_avail = 30000000
    min_candidate_size = target_avail - remaining
    candidate = None
    for name, size in dirs:
        if size > min_candidate_size:
            candidate = (name, size)
            break

    print(candidate)



if __name__ == '__main__':
    part2()