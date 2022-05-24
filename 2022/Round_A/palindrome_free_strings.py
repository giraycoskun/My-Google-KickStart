# Palindrome Free Strings
# KickStart 2022 Round A Problem 3
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb33e/00000000009e762e


palindrome_set5 = {
    "00001",
    "00010",
    "01000",
    "10000",

    "11000",
    "01100",
    "00110",
    "00011",
    "10100",
    "00101",
    "10010",
    "01001",

    "11100",
    "00111",
    "10110",
    "01011",
    "11010",
    "01101",
    "11110",
    "01111"
}

palindrome_set6 = {
    "000010",
    "000011",
    "000101",
    "000100",
    "010000",
    "010001",
    "100000",

    "110001",
    "110000",
    "011001",
    "011000",
    "001100",
    "001101",
    "000110",
    "000111",
    "101001",
    "101000",
    "001010",
    "001011",
    "100100",
    "100101",
    "010011",

    "111000",
    "111001",
    "001111",
    "001110",
    "101100",
    "010110",
    "010111",
    "110100",
    "110101",
    "011010",
    "011011",
    "111101",
    "111100",
    "011111"
}

test_count = int(input())
for t in range(test_count):
    N = int(input())
    S = input()

    answer = ""
    if len(S) < 5:
        answer = "POSSIBLE"
    else:
        viable_set = {}
        state_set = {}
        count = S[0:5].count('?')
        state = S[0:5]
        states = []
        for c in count:
            pass


def create_starter_set(s):
    if '?' in s:
        idx = s.find('?')
        s[idx] = '0'

    print("Case #{case_no}: {answer}".format(case_no=t + 1, answer=answer))
