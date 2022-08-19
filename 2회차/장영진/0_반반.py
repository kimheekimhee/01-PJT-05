# SWEA 11586. 반반
# 풀이법 : 딕셔너리에 넣고 키의 값이 2인지 확인

import sys

sys.stdin = open("_반반.txt")

T = int(input())

for i in range(1, T+1):
    S = list(input())
    S_dict = list(set(S))
    flag = True

    for j in S_dict:
        if not S.count(j) == 2:
            flag = False

    if flag:
        print(f'#{i} Yes')
    else:
        print(f'#{i} No')