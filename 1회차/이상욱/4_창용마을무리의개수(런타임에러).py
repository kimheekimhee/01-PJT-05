import sys
sys.stdin = open("_창용마을무리의개수.txt")

def dfs(start):
    stack = [start]
    visited[start] == True

    cur = stack.pop()

    while stack:
        for adj in con[cur]:
            if not visited[adj]:
                visited[adj] = True
                stack.append(adj)



T = int(input())
for t in range(1, T+1):
    n, m = map(int, input().split())
    con = [[] for _ in range(n+1)]
    for _ in range(m):
        N, M = map(int, input().split())
        con[N].append(M)
        con[M].append(N)


    visited = [False] * (n+1)
    cnt = 0

    for i in range(1, N+1):
        if visited[i] == False:
            cnt += 1
            dfs(i)
    #         stack = [i]
    #         visited[i] = True

    #         while stack:
    #             cur = stack.pop()
    #             for adj in con[cur]:
    #                 if not visited[adj]:
    #                     visited[adj] = True
    #                     stack.append(adj)
                        
    print(f'#{t} {cnt}')