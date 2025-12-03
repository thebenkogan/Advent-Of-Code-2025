from aoc import read_input


def best_n(line, num_batteries):
    # dp[i] = the biggest number we can make with the batteries in line[i:]
    # for each iteration, start with the previous best and try inserting
    # the next battery at the start and removing one other battery
    dp = [0] * len(line)
    dp[-num_batteries] = int(line[-num_batteries:])
    for i in range(len(line) - num_batteries - 1, -1, -1):
        prev_s = str(dp[i + 1])
        if int(line[i]) < int(prev_s[0]):
            dp[i] = dp[i + 1]
            continue
        nxt = line[i] + prev_s
        best = dp[i + 1]
        for j in range(1, len(nxt)):
            n = int(nxt[:j] + nxt[j + 1 :])
            best = max(best, n)
        dp[i] = best

    return dp[0]


lines = read_input()
print(sum(best_n(line, 2) for line in lines))
print(sum(best_n(line, 12) for line in lines))
