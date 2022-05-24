# Palindromic Deletions
# KickStart 2022 Round C Problem 4
# SOLVED for test case 1; TLE for test case 2

# from math import gd
from math import factorial


def modInverse(a, m):
    m0 = m
    y = 0
    x = 1

    if m == 1:
        return 0

    while a > 1:
        # q is quotient
        q = a // m

        t = m

        # m is remainder now, process
        # same as Euclid's algo
        m = a % m
        a = t
        t = y

        # Update x and y
        y = x - q * y
        x = t

    # Make x positive
    if x < 0:
        x = x + m0

    return x


def solve(L, R, length):
    if length == 0:
        return 1
    if length < 0:
        return 0
    if L > R:
        return 0
    extra = 0
    if L == R:
        extra = solve(L + 1, R - 1, length - 1)
    elif S[L] == S[R]:
        extra = solve(L + 1, R - 1, length - 2)
    result = solve(L, R - 1, length) + solve(L + 1, R, length) - solve(L + 1, R - 1, length) + extra
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
    table = {}
    p = 0
    for K in range(N):
        if (0, N-1, K) in table:
            result = table[(0, N-1, K)]
        else:
            result = solve(0, N - 1, K)
            table[(0, N - 1, K)] = result
        p += result * fact(K) * fact(N - K)

    q = fact(N)
    m = (10 ** 9) + 7
    x = modInverse(q, m)
    answer = (p * x) % m
    print("Case #{case_no}: {answer}".format(case_no=t + 1, answer=answer))

"""
def checkPalindrome(s):
    if s in pal:
        return pal[s]
    i = 0
    j = len(s) - 1
    for _ in range(len(s)):
        if i > j:
            pal[s] = True
            return True
        if s[i] != s[j]:
            pal[s] = False
            return False
        i += 1
        j -= 1

def solve(s):
    if len(s) == 1:
        return 2
    if s in res:
        return res[s]
    ans = 0
    for k in range(len(s)):
        temp = s[:k] + s[k + 1:]
        ans += solve(temp)
    if checkPalindrome(s):
        ans += 1
    res[s] = ans
    return ans

pal = {}
res = {}

test_count = int(input())
for t in range(test_count):
    N = int(input())
    S = input()
    pal = {}
    res = {}

    ans = solve(S)
    tests = factorial(N)
    if ans % tests == 0:
        answer = int(ans / tests)
    else:
        temp = gcd(ans, tests)
        while temp != 1:
            ans = int(ans / temp)
            tests = int(tests / temp)
            temp = gcd(ans, tests)

        m = (10 ** 9) + 7
        x = modInverse(tests, m)
        answer = int(((x * tests) + ans - 1) / tests)

    print("Case #{case_no}: {answer}".format(case_no=t + 1, answer=answer))
"""
