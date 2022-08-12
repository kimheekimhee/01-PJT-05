import sys
sys.stdin = open("_창용마을무리의개수.txt")
from pprint import pprint


T = int(input())
for t in range(T):
    n, m = map(int, input().split())

    relation = [[] for _ in range(n+1)]

    visited = [False] * (n+1)

    for j in range(m):
        v1, v2 = map(int,input().split())
        relation[v1].append(v2)
        relation[v2].append(v1)

    def dfs(start):
        stack = [start]
        visited[start] = True
        
        while len(stack) != 0:
            cur = stack.pop()
            
            for adj in relation[cur]:
                if not visited[adj]:
                    visited[adj] = True
                    stack.append(adj)

    cnt = 0
    for i in range(1,n+1):

        if visited[i] == False:
            cnt += 1
            dfs(i)
    print(f'#{t+1} {cnt}')