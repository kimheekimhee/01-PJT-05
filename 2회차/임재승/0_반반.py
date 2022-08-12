import sys

sys.stdin = open("_반반.txt")

TC = int(input())

for T in range(1, TC+1):
    S = input()
    cnt = 0
    for idx in S:
        if S.count(idx) != 2:
            print(f'#{T} No')
            break
        else:
            cnt += 1
    if cnt == 4:
        print(f'#{T} Yes')
