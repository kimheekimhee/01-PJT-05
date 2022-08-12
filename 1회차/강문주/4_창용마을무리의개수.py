import sys
sys.stdin = open("_창용마을무리의개수.txt")
from collections import deque

input=sys.stdin.readline

for tc in range(1, 1 + int(input())):
    N, M = map(int, input().split())
    adj = {x + 1: [] for x in range(N)}
    for _ in range(M):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)

    visited = [0] * (N + 1)
    visited[0] = 1
    q = deque()
    cnt = 0

    for i in range(1, N+1):
        if visited[i] == 0:
            cnt += 1
            q.append(i)
            visited[i] == 1

        while q:
            c = q.popleft()
            for neighbor in adj[c]:
                if visited[neighbor] == 0:
                    q.append(neighbor)
                    visited[neighbor] = 1

    print('#{} {}'.format(tc, cnt))