from functools import cache
import re
from aoc import read_input

adj = {}
lines = read_input()
for line in lines:
    ns = re.findall(r"\w+", line)
    adj[ns[0]] = ns[1:]

stack = ["you"]
total = 0
while len(stack) > 0:
    n = stack.pop()
    if n == "out":
        total += 1
        continue

    for neighbor in adj[n]:
        stack.append(neighbor)

print(total)


@cache
def part2(node, seen_dac, seen_fft):
    if node == "out":
        return 1 if seen_dac and seen_fft else 0
    else:
        ans = 0
        for neighbor in adj[node]:
            new_seen_dac = seen_dac or neighbor == "dac"
            new_seen_fft = seen_fft or neighbor == "fft"
            ans += part2(neighbor, new_seen_dac, new_seen_fft)
        return ans


print(part2("svr", False, False))
