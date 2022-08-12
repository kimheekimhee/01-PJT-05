import sys

sys.stdin = open("_창용마을무리의개수.txt")

T = int(input())

for t in range(1, T+1) :
    n, m = map(int, input().split())
    rel = [[]for i in range(n+1)]
    for i in range(m) :
        a, b = map(int, input().split())

        rel[a].append(b)
        rel[b].append(a)

    visited = [0 for i in range(n+1)]
    def dfs(start) :
        stack = [start]
        

        while stack :
            node = stack.pop()

            if not visited[node] :
                visited[node] = 1
                stack.extend(rel[node])

    cnt = 0
    for i in range(1, n+1) :
        if not visited[i] :
            dfs(i)
            cnt += 1
    
    print(f'#{t} {cnt}')