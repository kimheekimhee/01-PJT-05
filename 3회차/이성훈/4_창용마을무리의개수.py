## 후기 작성

import sys

sys.stdin = open("_창용마을무리의개수.txt")

T = int(input())

for j in range(1, T+1):

    cnt = 0
    N, M = map(int, input().split())

    matrix = []
    visited = [False] * (N + 1)

    for _ in range(N + 1):
        matrix.append([])

    for _ in range(M):
        v1, v2 = map(int, input().split())
        matrix[v1].append(v2)
        matrix[v2].append(v1)

    def dfs(start):
        stack = [start]
        visited[start] = True

        while stack:
            cur = stack.pop()

            for adj in matrix[cur]:
                if not visited[adj]:
                    visited[adj] = True
                    stack.append(adj)


    for i in range(1, N+1):
        if visited[i] == False:
            dfs(i)
            cnt += 1





    print(f'#{j} {cnt}')