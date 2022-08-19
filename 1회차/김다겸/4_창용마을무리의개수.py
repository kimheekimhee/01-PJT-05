import sys

sys.stdin = open("_창용마을무리의개수.txt")

# dfs 탐색
def dfs(start):
    stack = [start]
    visited[start] = True

    while stack:
        cur = stack.pop()
        for adj in graph[cur]:
            if not visited[adj]:
                visited[adj] = True
                stack.append(adj)

T = int(input())
for t in range(1, T+1):
    n, m = map(int, input().split())

    graph = [[] for _ in range(n+1)]

    # 인접 리스트 생성
    for i in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    # 방문 리스트 생성
    visited = [False] * (n + 1)
    cnt = 0

    for j in range(1, n+1):
        # 방문하지 않았다면
        if not visited[j]:
            # dfs 탐색 후
            dfs(j)
            # 1 더하기
            cnt += 1
    print(f'#{t} {cnt}')