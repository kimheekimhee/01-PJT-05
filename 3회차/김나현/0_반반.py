import sys

sys.stdin = open("_반반.txt")

n = int(input())
for test_case in range(1, n + 1):
    s = input()
    check = 0
    for w in s:
        if s.count(w) != 2:
            check = 1
            print(f'#{test_case} No')
            break
    if check == 0:
        print(f'#{test_case} Yes')