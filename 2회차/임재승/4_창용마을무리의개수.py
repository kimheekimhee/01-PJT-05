from collections import deque
import sys

sys.stdin = open("_창용마을무리의개수.txt")

def bfs(start):
    man = deque([start])
    visited[start] = True
    while man:
        now = man.popleft()
        for muri in li_cy[now]:
            if not visited[muri]:
                man.append(muri)
                visited[muri] = True

T = int(input())

for i in range(1, T+1):
    N, M = map(int, input().split())
    visited = [False] * (N + 1)
    li_cy = [[] for _ in range(N+1)]
    cnt = 0
    for _ in range(M):
        x, y = map(int, input().split())
        li_cy[x].append(y)
        li_cy[y].append(x)

    for p in range(1, N+1):
        if not visited[p]:
            bfs(p)
            cnt += 1

    print(f'#{i} {cnt}')