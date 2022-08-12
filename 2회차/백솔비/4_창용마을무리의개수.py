import sys
sys.stdin = open("_창용마을무리의개수.txt")
from pprint import pprint

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    graph = [[0] * (N+1) for _ in range(N+1)]

    for _ in range(M):
        v1, v2 = map(int, input().split())
        graph[v1][v2] = 1
        graph[v2][v1] = 1
    
    # pprint(graph)
    
    visited = [0] * (N+1)

    def dfs(k):
        visited[k] = 1
        for i in range(N+1):
            if graph[i][k] == 1 and visited[i] == 0:
                dfs(i)
    
    cnt = 0

    for i in range(1, N+1):
        if visited[i] == 0:
            dfs(i)
            cnt += 1
    
    print(f'#{tc} {cnt}')