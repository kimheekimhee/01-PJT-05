import sys

sys.stdin = open("_창용마을무리의개수.txt")
def dfs (start):
    stack = [start]
    visited[start] = True
    while stack:
        now = stack.pop()
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                stack.append(i)

T = int(input())
for i in range(T):
    N, M = map(int,input().split())
    graph = [[] for _ in range(N+1)]
    for j in range(M):
        v1, v2 = map(int,input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)
    visited = [False] * (N + 1)

    cnt = 0
    for j in range(1, N + 1):
        if not visited[j]:
            dfs(j)
            cnt += 1
    print(f'#{i+1} {cnt}')