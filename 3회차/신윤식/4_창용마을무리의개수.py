import sys

sys.stdin = open("./3회차/신윤식/_창용마을무리의개수.txt")
T = int(input())

for _ in range(1, T+1):
    N, M = map(int,input().split())
    graph = [[] for i in range(N+1)]
    count = 0

    for j in range(M):
        a, b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [0] * (N+1)

    stack = [1]
    visited[1] = 1

    while True:

        while stack:
            cur = stack.pop()

            for adj in graph[cur]:
                if visited[adj] == 0:
                    visited[adj] = 1
                    stack.append(adj)
        
        count += 1

        if sum(visited) == N:
            break

        for k in range(1, N+1):
            if visited[k] == 0:
                visited[k] = 1
                stack.append(k)
                break
    print(f'#{_} {count}')