import sys

sys.stdin = open("_반반.txt")

# 길이 4의 알파벳 대문자로 이루어진 문자열 S가 주어졌을 때, S에 정확히 두 개의 서로 다른 문자가 등장하고, 각 문자가 정확히 두 번 등장하는 지 판별하라.

N = int(input())
for tc in range(1, N+1):
    S = list(input())
    S_set = set(S)
    cnt = 0
    if len(S_set) != 2:
        print(f'#{tc} No')
    else:
        for j in S_set:
            cnt += S.count(j)
        if cnt == 4:
            print(f'#{tc} Yes')
        else:
            print(f'#{tc} No')
