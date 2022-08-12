import sys

sys.stdin = open("_창용마을무리의개수.txt")
T = int(input())
for i in range(1, T+1):
    N, M = map(int, input().split())
    N = N + 1
    result = [[] for _ in range(N)]
    visited = [False] * N
    for j in range(M):
        A, B = map(int, input().split())
        result[A].append(B)
        result[B].append(A)
    cnt = 0
    for j in range(1, N):
        if not visited[j]:
            start = [j]
            visited[j] = True
            cnt += 1
            while start:
                X = start.pop()
                for k in result[X]:
                    if not visited[k]:
                        start.append(k)
                        visited[k] = True
    print(f'#{i}', cnt)
