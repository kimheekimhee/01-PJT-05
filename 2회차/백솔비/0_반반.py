import sys
sys.stdin = open("_반반.txt")

T = int(input())

for tc in range(T):
    S = input()
    alp = [0] * 26

    for i in S:
        alp[ord(i) - 65] += 1

    if alp.count(2) == 2:
        print(f'#{tc+1} Yes')
    else:
        print(f'#{tc+1} No')
