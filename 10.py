from collections import deque
import re
from aoc import nums, read_input
import z3


class Machine:
    def __init__(self, config):
        end_s = config.split(" ")[0][1:-1]
        self.end = tuple(c == "#" for c in end_s)
        buttons = re.findall(r"\((?:\d+,?)+\)", config)
        self.buttons = [tuple(nums(s)) for s in buttons]
        self.levels = tuple(nums(re.findall(r"{(?:\d+,?)+}", config)[0]))

    def fewest_presses(self):
        start = tuple([False] * len(self.end))
        seen = {start}
        q = deque([(0, start)])
        while len(q) > 0:
            presses, state = q.popleft()
            if state == self.end:
                return presses

            for b in self.buttons:
                next_state = list(state)
                for i in b:
                    next_state[i] = not next_state[i]
                next_state = tuple(next_state)
                if next_state in seen:
                    continue
                seen.add(next_state)
                q.append((presses + 1, next_state))

    def fewest_presses_level(self):
        presses = [z3.Int(f"press{i}") for i in range(len(self.buttons))]
        s = z3.Optimize()
        for press in presses:
            s.add(press >= 0)
        for i, level in enumerate(self.levels):
            usable_presses = [
                presses[j] for j, button in enumerate(self.buttons) if i in button
            ]
            s.add(sum(usable_presses) == level)
        s.minimize(sum(presses))
        s.check()

        m = s.model()
        return sum(m[press].as_long() for press in presses)


lines = read_input()
total1 = 0
total2 = 0
for line in lines:
    m = Machine(line)
    total1 += m.fewest_presses()
    total2 += m.fewest_presses_level()

print(total1)
print(total2)
