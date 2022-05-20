# INFINITY AREA
# KickStart 2022 Round B Problem 1
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008caa74/0000000000acf079

PI = 3.141592653589793
test_count = int(input())
for k in range(test_count):
    test = list(map(int, input().split()))
    # print(test)
    answer = 0.0

    R = test[0]
    A = test[1]
    B = test[2]
    r = R
    area = PI * R * R
    while r > 0:
        r = r * A
        area += PI * r * r
        r = r // B
        if r == 0:
            break
        area += PI * r * r

    print("Case #{case_no}: {answer}".format(case_no=k + 1, answer=area))
