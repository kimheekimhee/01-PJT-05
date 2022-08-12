# 마을에 몇 개의 무리가 존재하는지 계산하는 프로그램을 작성하라.
# DFS

import sys

sys.stdin = open("_창용마을무리의개수.txt")

T = int(input())
for i in range(T):
    l = []
    N, M = map(int,input().split())
    check_list = [[] for i in range(N)]
    for i in range(M):
        p = list(map(int,input().split()))
        l.append(p)
        for i in l:
            for j in i:
                if check_list[j-1]==[]:
                    check_list[j-1].append(1)
                    group.append(j)

    print(l)