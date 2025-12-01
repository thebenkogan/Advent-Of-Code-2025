from aoc import read_input


lines = read_input()

dial = 50
total1 = 0
total2 = 0
for line in lines:
    factor = 1 if line[0] == "R" else -1
    n = int(line[1:])
    for _ in range(n):
        dial = (dial + factor) % 100
        if dial == 0:
            total2 += 1
    if dial == 0:
        total1 += 1

print(total1)
print(total2)
