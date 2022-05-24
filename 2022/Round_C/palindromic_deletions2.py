from math import factorial


def power(x, y, m):
    if y == 0:
        return 1

    p = power(x, y // 2, m) % m
    p = (p * p) % m

    if y % 2 == 0:
        return p
    else:
        return (x * p) % m


def modInverse(a, m):
    return power(a, m - 2, m)


def solve(L, R, length):
    if table[L][R][length] != -1:
        return table[L][R][length]
    if length == 0:
        return 1
    elif length < 0:
        return 0
    elif L > R:
        return 0
    else:
        extra = 0
        if L == R:
            extra = solve(L + 1, R - 1, length - 1)
        elif S[L] == S[R] and length > 1:
            extra = solve(L + 1, R - 1, length - 2)
        result = solve(L, R - 1, length) + solve(L + 1, R, length) - solve(L + 1, R - 1, length) + extra
        table[L][R][length] = result
        return result


fact_table = {}


def fact(N):
    if N in fact_table:
        return fact_table[N]
    else:
        fact_table[N] = factorial(N)
        return fact_table[N]


test_count = int(input())
for t in range(test_count):
    N = int(input())
    S = input()
    table = [[[-1 for _ in range(N+1)] for _ in range(N+1)] for _ in range(N+1)]
    p = 0
    for K in range(N):
        p += solve(0, N - 1, K) * fact(K) * fact(N - K)

    q = fact(N)
    m = (10 ** 9) + 7
    x = modInverse(q, m)
    answer = (p * x) % m
    print("Case #{case_no}: {answer}".format(case_no=t + 1, answer=answer))
