import sys

sys.stdin = open("_창용마을무리의개수.txt")

from collections import deque

T = int(input())

for tc in range(T):
    def bfs(v):
        q = deque()
        q.append(v)
        visited[v] = 1
        
        while q:
            x = q.popleft()
            for i in graph[x]: 
                if not visited[i]:
                    visited[i] = 1
                    q.append(i)
        
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    visited = [0] * (n + 1)
    
    for i in range(m):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)
        
    cnt = 0 
    for i in range(1,n + 1):
        if not visited[i]:
            bfs(i)
            cnt += 1
    print(f'#{tc+1}', cnt)    