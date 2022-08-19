import sys

sys.stdin = open("_창용마을무리의개수.txt")

case = int(input())

def dfs(node):
    visited[node] = True
    for k in graph[node]:
        if not visited[k]:
            dfs(k)

for case in range(1,case+1):
    N,M = map(int,input().split())
    graph = [[] for _ in range(N+1)]
    visited = [False]*(N+1)
    for i in range(M):
        n,m = map(int,input().split())
        graph[n].append(m)
        graph[m].append(n)
    
    count = 0
    for d in range(1,N+1):
        if not visited[d]:
            dfs(d)
            count +=1
             
    print(f'#{case} {count}')
   
    
        
    
    
    
   
        