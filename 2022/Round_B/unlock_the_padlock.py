# Unlock The Padlock
# KickStart 2022 Round B Problem 3
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008caa74/0000000000acef55#analysis
# I believe Google Analysis is missing
# So I found this repo very helpful: https://github.com/kamyu104/GoogleKickStart-2022


def solve(i, j, k) -> int:
    if i > j:
        return 0
    if k in dp[i][j]:
        return dp[i][j][k]

    current_operations1 = min((padlock[i] - k) % D, D - ((padlock[i] - k) % D))
    val_1 = current_operations1 + solve(i + 1, j, padlock[i])

    current_operations2 = min((padlock[j] - k) % D, D - ((padlock[j] - k) % D))
    val_2 = current_operations2 + solve(i, j - 1, padlock[j])

    dp[i][j][k] = min(val_1, val_2)
    return dp[i][j][k]


test_count = int(input())
# test_count = 1
for c in range(test_count):
    test = list(map(int, input().split()))
    # test = list(map(int, "6 10".split()))
    padlock = list(map(int, input().split()))
    # padlock = list(map(int, "1 1 9 9 1 1".split()))
    N = test[0]
    D = test[1]

    dp = [[{} for _ in range(N)] for _ in range(N)]

    answer = solve(0, N - 1, 0)

    print("Case #{case_no}: {answer}".format(case_no=c + 1, answer=answer))
    