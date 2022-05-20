# Palindromic Factors
# KickStart 2022 Round B Problem 2
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008caa74/0000000000acee89


def check_palindrome(x) -> bool:
    x = str(x)
    length = len(x)
    i = 0
    l = length - 1
    while i < l:
        if x[i] == x[l]:
            i += 1
            l -= 1
        else:
            return False
    return True


def find_factors(x) -> list[int]:
    factors_list = set()
    for k in range(1, int(x ** 0.5) + 1):
        if x % k == 0:
            factors_list.add(k)
            factors_list.add(x // k)
    return factors_list


test_count = int(input())
for k in range(test_count):
    A = int(input())
    count_palindrome = 0
    factors = find_factors(A)
    for factor in factors:
        if check_palindrome(factor):
            count_palindrome += 1

    print("Case #{case_no}: {answer}".format(case_no=k + 1, answer=count_palindrome))

'''
def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def factors(n):
    return set(
        factor for i in range(1, int(n**0.5) + 1) if n % i == 0
        for factor in (i, n//i)
    )
'''
