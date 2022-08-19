import sys
sys.stdin = open("_창용마을무리의개수.txt")

t = int(input())

for case in range(1, t+1):
    n, m = map(int, input().split())
    
    p = [[] for _ in range(n+1)]
    visited=[0] * (n+1)
    def dfs(v):
        visited[v] = 1
        for a in p[v]:
            if not visited[a]:
                dfs(a)

    for _ in range(m):
        n1, n2 = map(int, input().split())
        p[n1].append(n2)
        p[n2].append(n1)
    
    cnt = 0
    for i in range(1, n+1):
        if not visited[i]:
            dfs(i)
            cnt+=1
            
    print(f'#{case} {cnt}')