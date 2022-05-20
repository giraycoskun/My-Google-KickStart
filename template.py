# TEMPLATE
# input and output template

test_count = int(input())
for t in range(test_count):
    test = list(map(int, input().split()))
    X, Y = map(int, input().split())
    answer = 0
    print("Case #{case_no}: {answer}".format(case_no=t + 1, answer=answer))
