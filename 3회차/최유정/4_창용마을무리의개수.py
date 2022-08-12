import sys

sys.stdin = open("_창용마을무리의개수.txt")

T = int(input())
lst = []
for t in range(1, T+1):
    N, M = map(int, input().split())
    for i in range(N):
        lst.append([0]*N)
    for i in range(M):
        n1, n2 = map(int,input().split())
        lst[n1-1][n2-1] = 1
        lst[n2-1][n1-1] = 1
    print(lst)