# Ants on a Stick
# KickStart 2022 Round C Problem 3
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb4d1/0000000000b209bc#problem
# SOLVED in all test cases after analysis

from bisect import insort

test_count = int(input())
for t in range(test_count):
    N, L = map(int, input().split())
    ants = []
    for id in range(N):
        P, D = map(int, input().split())
        a = (P, D, id+1)
        insort(ants, a)
    result = []
    for ant in ants:
        if ant[1] == 0:
            a = (ant[0], 0)
        else:
            a = (L-ant[0], 1)
        insort(result, a)

    answer = []
    for fall in result:
        if fall[1] == 0:
            a = ants.pop(0)
        else:
            a = ants.pop(-1)
        a = (fall[0], a[2])
        insort(answer, a)

    answer_str = ""
    for a in answer:
        answer_str += str(a[1]) + ' '
    answer = answer_str[:-1]
    print("Case #{case_no}: {answer}".format(case_no=t + 1, answer=answer))

