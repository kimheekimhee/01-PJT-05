import sys

sys.stdin = open("_모음이보이지않는사람.txt")


T = int(input())

for test_case in range(1, T + 1):
    word = input()
    answer = ''

    for i in word:
        if i not in ['a', 'e', 'i', 'o', 'u']:
            answer += i

    print(f"#{test_case} {answer}")