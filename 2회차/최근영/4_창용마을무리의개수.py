import sys
from turtle import st

sys.stdin = open("_창용마을무리의개수.txt")

T = int(sys.stdin.readline())

for i in range(1,T+1):
    cnt_list = []
    N,M = list(map(int,sys.stdin.readline().split()))
    matrix = [[] for _ in range(N+1)]
    for j in range(M):
        x,y = list(map(int,sys.stdin.readline().split()))
        matrix[x].append(y)
        matrix[y].append(x)
    for k in range(1,len(matrix)):
        visited = [False for __ in range(N+1)]
        stack = list(matrix[k])
        visited[k] = True
        while stack:
            com = stack.pop()
            visited[com] = True
            for l in matrix[com]:
                if visited[l] == False:
                    visited[l] = True
                    if l not in stack:
                        stack.append(l)
        if visited not in cnt_list:
            cnt_list.append(visited)
    print(f"#{i}",len(cnt_list))