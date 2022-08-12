# SWEA 7465. 창용마을 무리의 개수
# 그래프의 개수, 완전 탐색 후 방문하지 않은 노드가 있다면, 다른 그래프가 존재 반복

from collections import deque
import sys

sys.stdin = open("_창용마을무리의개수.txt")

T = int(input())

for i in range(1, T+1):
    N, M = map(int, input().split()) 
    arr = [[] for _ in range(N + 1)]
    
    for _ in range(M):
        x, y = map(int, input().split())
        arr[x].append(y)
        arr[y].append(x)

    visited = [0] * (N+1)
    visited[0] = 1
    queue = deque()
    cnt = 0

    for j in range(1, N+1):
        if visited[j] == 0:
            cnt += 1
            queue.append(j)
            visited[j] = 1
        while queue:
            idx = queue.popleft()
            for k in arr[idx]:
                if visited[k] == 0:
                    queue.append(k)
                    visited[k] = 1

    print(f'#{i} {cnt}')