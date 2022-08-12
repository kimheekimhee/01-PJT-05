import sys

sys.stdin = open("_창용마을무리의개수.txt")

T = int(input())
for ts in range(1, T+1):
    N, M = map(int, input().split())
    contact = [[] for _ in range(N+1)]
    for t in range(M):
        x, y = map(int, input().split())
        contact[x].append(y)
        contact[y].append(x)
    visited = [False] * (N+1)

    def dfs(start):
        stack = [start]
        visited[start] = True

        while stack:
            cur = stack.pop()
            
            for adj in contact[cur]:
                if not visited[adj]:
                    visited[adj] = True
                    stack.append(adj)
    cnt = 0
    for a in range(1,N+1):
        if not visited[a]:
            if not contact[a]:
                cnt += 1
                visited[a] = True
            else:
                dfs(a)
                cnt += 1
    print(f'#{ts} {cnt}')