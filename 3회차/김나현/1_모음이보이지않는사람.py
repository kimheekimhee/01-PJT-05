import sys

sys.stdin = open("_모음이보이지않는사람.txt")

T = int(input())

for test_case in range(1, T + 1):
    s = input()
    print(f'#{test_case} ', end='')
    for w in s:
        if w == 'a' or w == 'e' or w == 'i' or w == 'o' or w == 'u':
            continue
        print(w, end='')
    print()