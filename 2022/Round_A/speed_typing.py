# Speed Typing
# KickStart 2022 Round A Problem 1
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb33e/00000000009e7021

test_count = int(input())
for t in range(test_count):
    I = input()
    P = input()
    answer = "IMPOSSIBLE"

    if len(I) > len(P):
        answer = "IMPOSSIBLE"
    else:
        i = 0
        j = 0
        count = 0
        delete_count = 0
        for _ in range(len(P)):
            if i == len(I) or j == len(P):
                break
            if I[i] == P[j]:
                i += 1
                j += 1
                count += 1
            else:
                delete_count += 1
                j += 1

        if count == len(I):
            answer = delete_count + len(P) - j

    print("Case #{case_no}: {answer}".format(case_no=t + 1, answer=answer))
