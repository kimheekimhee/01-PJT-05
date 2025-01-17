import sys
from collections import deque
sys.stdin = open("_창용마을무리의개수.txt")

def bfs(v, edges, visited):
    q = deque([v])
    visited[v] = True

    while q:
        now = q.popleft()

        for e in edges[now]:
            if not visited[e]:
                q.append(e)
                visited[e] = True
T = int(input())
for tc in range(1,1+T):
    n, m = map(int, input().split())
    edges = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        edges[u].append(v)
        edges[v].append(u)

    result = 0
    visited = [False] * (n + 1)

    for i in range(1, n + 1):
        if not visited[i]:
            result += 1
            bfs(i, edges, visited)

    print(f"#{tc}",result)