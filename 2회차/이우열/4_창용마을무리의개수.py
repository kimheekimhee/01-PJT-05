import sys

sys.stdin = open("_창용마을무리의개수.txt")

t = int(input())

for tt in range(1, t + 1):
    n, m = map(int, input().split())

    graph = [[] for _ in range(n + 1)]

    for _ in range(1, m + 1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    stack = []
    visited = [False for _ in range(n + 1)]
    cnt = 0

    for i in range(1, n + 1):
        if not visited[i]:
            cnt += 1
            stack.append(i)

            while stack:
                cur = stack.pop()
                visited[cur] = True

                for adj in graph[cur]:
                    if not visited[adj]:
                        stack.append(adj)

    print(f'#{tt} {cnt}')
