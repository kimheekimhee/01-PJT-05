from re import L
import sys

sys.stdin = open("_창용마을무리의개수.txt")

T = int(input())
for tc in range(1,T + 1):
    N, M = map(int, input().split())

    graph = [[] for _ in range(N + 1)]
    visited = [0] * (N + 1)

    for _ in range(M):
            x, y = map(int, input().split())
            graph[x].append(y)
            graph[y].append(x)

    def dfs(v):
        for j in graph[v]:
            visited[v] = 1
            if visited[j] == 0:
                dfs(j)

    cnt = 0
    for k in range(1, N+1):
        if visited[k] == 0:
            cnt += 1
            dfs(k)

    print(f'#{tc} {cnt}')
