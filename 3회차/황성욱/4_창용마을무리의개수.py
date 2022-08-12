import sys
# 풀어봤던 문제
sys.stdin = open("_창용마을무리의개수.txt")
def dfs(graph, v, visited):
    visited[v] = True
    
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    adj_list = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    for j in range(m):
        x, y = map(int, input().split())
        adj_list[x].append(y)
        adj_list[y].append(x)
    cnt = 0
    for k in range(1, n + 1):
        if not visited[k]:
            dfs(adj_list, k, visited)
            cnt += 1
    print(f'#{i + 1}',cnt)
