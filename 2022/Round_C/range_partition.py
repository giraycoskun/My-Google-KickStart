# Range Partition
# KickStart 2022 Round C Problem 2
# SOLVED in all test cases during competition

"""def solve(ans, items, sumi):
    if ans > sumi:
        return []
    if sumi == ans:
        return items
    for k in range(len(items)):
        temp = items[:k] + items[k+1:]
        res = solve(ans, temp, (sumi-items[k]))
        if len(res) != 0:
            return res
    return []


test_count = int(input())
for t in range(test_count):
    N, X, Y = map(int, input().split())


    total = (N*(N+1))/2
    answer = "IMPOSSIBLE"
    if (total % (X+Y)) != 0:
        print("Case #{case_no}: {answer}".format(case_no=t + 1, answer=answer))
    else:
        answer = "POSSIBLE"
        print("Case #{case_no}: {answer}".format(case_no=t + 1, answer=answer))
        N = list(range(1, N + 1))
        x = int((total / (X+Y)) * X)
        sol = solve(x, N, int(total))
        print(len(sol))
        for item in sol:
            print(item, end=' ')
        print()"""

test_count = int(input())
for t in range(test_count):
    N, X, Y = map(int, input().split())


    total = (N*(N+1))/2
    answer = "IMPOSSIBLE"
    if (total % (X+Y)) != 0:
        print("Case #{case_no}: {answer}".format(case_no=t + 1, answer=answer))
    else:
        answer = "POSSIBLE"
        print("Case #{case_no}: {answer}".format(case_no=t + 1, answer=answer))
        nums = list(range(1, N + 1))
        x = int((total / (X + Y)) * X)
        sol = []
        for num in reversed(nums):
            if N < x:
                sol.append(num)
                x = x-num
            else:
                if x > num:
                    sol.append(num)
                    x = x - num
                else:
                    sol.append(x)
                    break

        print(len(sol))
        for item in sol:
            print(item, end=' ')
        print()
