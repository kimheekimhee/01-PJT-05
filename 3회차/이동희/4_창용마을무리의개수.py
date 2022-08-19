import sys

sys.stdin = open("_창용마을무리의개수.txt")

def dfs(n):
    visited[n] = 1
    for i in graph[n]:
        if not visited[i]:
            dfs(i)
            
for tc in range(1, int(input())+1):
    
    node,vertex = map(int, input().split())
    
    graph = [[] for _ in range(node + 1)]

    for i in range(vertex):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    visited = [0 for _ in range(node + 1)]

    count = 0
        
    for n in range(1, node+1):
        if not visited[n]:
            dfs(n)
            count += 1

    print(f'#{tc} {count}')