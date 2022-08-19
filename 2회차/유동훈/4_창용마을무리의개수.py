import sys

sys.stdin = open("_창용마을무리의개수.txt")

T = int(input())
for i in range(1, T+1):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split()) 
        graph[a].append(b)
        graph[b].append(a)

    # print(graph)


    visited = [0] * (N+1)

    def dfs(graph, v, visited):
        visited[v] = 1
        for j in graph[v]:
            if visited[j] == 0:
                dfs(graph, j, visited)
   

    members = []
    for k in range(1, N+1):
        muri = []
        visited = [0] * (N+1)
        dfs(graph, k, visited)
        # if sum(visited) >= 2:
        cnt = 0
        for l in visited:
            if l == 1:
                muri.append(cnt)
            cnt += 1
        members.append(muri)
    
    members = set([tuple(set(member)) for member in members])
    print(f'#{i} {len(members)}')