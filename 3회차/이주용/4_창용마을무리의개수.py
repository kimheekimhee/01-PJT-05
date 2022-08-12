import sys

sys.stdin = open("_창용마을무리의개수.txt")
from collections import deque
t = int(input())
for x in range(1, t + 1):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    queue = deque()
    group = 0
    for i in range(1, n + 1):
        if not visited[i]:
            queue.append(i)
            visited[i] = True
            while queue:
                v = queue.popleft()
                for adj in graph[v]:
                    if not visited[adj]:
                        visited[adj] = True
                        queue.append(adj)
            group += 1
    print('#{} {}'.format(x, group))