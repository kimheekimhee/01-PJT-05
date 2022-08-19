import sys

sys.stdin = open("_창용마을무리의개수.txt")

from collections import deque

def bfs(start):
    queue = deque([start])
    visited[start] = True
    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

T = int(input())
for z in range(1,T+1):
    N, M = map(int,input().split())
    graph = [[] for _ in range(N+1)]
    visited = [False] * (N+1)
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    cnt = 0
    for i in range(1, N+1):
        if visited[i] == False:
            cnt += 1
            visited[i] = True
            bfs(i)
    print(f'#{z} {cnt}')