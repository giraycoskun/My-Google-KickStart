# Challenge Nine
# KickStart 2022 Round A Problem 2
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb33e/00000000009e7997

test_count = int(input())
for t in range(test_count):
    N = list(map(int, list(input())))
    sum = 0
    for c in N:
        sum += c

    extra_num = 9 - (sum % 9)

    inserted = False
    if extra_num == 9:
        inserted = True
        N.insert(1, 0)
    else:
        for idx in range(len(N)):
            if N[idx] > extra_num:
                N.insert(idx, extra_num)
                inserted = True
                break

    if not inserted:
        N.append(extra_num)

    answer = 0
    base = 1
    for i in reversed(N):
        answer += i*base
        base = base*10
    print("Case #{case_no}: {answer}".format(case_no=t + 1, answer=int(answer)))
