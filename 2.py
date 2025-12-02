from aoc import read_input


def is_invalid1(n):
    s = str(n)
    if len(s) == 2 and s[0] == s[1]:
        return True
    for i in range(1, len(s) - 1):
        if s[:i] == s[i:]:
            return True
    return False


def is_invalid2(n):
    s = str(n)
    if len(s) == 2 and s[0] == s[1]:
        return True
    for i in range(len(s) // 2):
        if len(s) % (i + 1) != 0:
            continue
        test = s[: i + 1]
        if all(s[j : j + len(test)] == test for j in range(0, len(s), len(test))):
            return True
    return False


lines = read_input(split_lines=False)
ids = lines.split(",")
total1 = 0
total2 = 0
for pair in ids:
    a, b = pair.split("-")
    a, b = int(a), int(b)
    for i in range(a, b + 1):
        if is_invalid1(i):
            total1 += i
        if is_invalid2(i):
            total2 += i

print(total1)
print(total2)
