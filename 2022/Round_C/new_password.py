# New Password
# KickStart 2022 Round C Problem 1
# SOLVED in all test cases during competition

test_count = int(input())
for t in range(test_count):
    special_chars = {'#', '@', '*', '&'}
    uppercase = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                 'U', 'V', 'W', 'X', 'Y', 'Z'}
    lowercase = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z'}
    digits = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
    N = int(input())
    old_password = input()

    check1 = False
    check2 = False
    check3 = False
    check4 = False

    for c in old_password:
        if not check1 and c in special_chars:
            check1 = True
        if not check2 and c in uppercase:
            check2 = True
        if not check3 and c in lowercase:
            check3 = True
        if not check4 and c in digits:
            check4 = True
        if check1 and check2 and check3 and check4:
            break

    addition = ""
    if not check1:
        addition += special_chars.pop()
    if not check2:
        addition += uppercase.pop()
    if not check3:
        addition += lowercase.pop()
    if not check4:
        addition += digits.pop()
    answer = old_password + addition
    if len(answer) < 7:
        for _ in range(7 - len(answer)):
            answer += '0'
    print("Case #{case_no}: {answer}".format(case_no=t + 1, answer=answer))
