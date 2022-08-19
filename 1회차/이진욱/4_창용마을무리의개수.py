import sys

sys.stdin = open("_창용마을무리의개수.txt")



T = int(input())

for t in range(T):
        
    
    N,M = map(int,input().split())
    
    graph = [ [] for _ in range(N+1) ]
    
    for i in range(M):
        a,b = list(map(int,input().split()))
    
        graph[a].append(b)
        graph[b].append(a)
    
    
    def dfs(x):
        visted[x] = True
    
        for i in graph[x]:
            if not visted[i]:
                dfs(i)
    
    
    visted_list = []
    
    for i in range(1,N+1):
        visted = [False] * (N+1)
        dfs(i)
        visted = tuple(visted)
        visted_list.append(visted)
    
    
    ans = len(set(visted_list))
    print(f'#{t+1} {ans}')
    
