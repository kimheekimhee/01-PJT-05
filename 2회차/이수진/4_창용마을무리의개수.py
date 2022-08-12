from posixpath import split
import sys

from sqlalchemy import false

sys.stdin = open("_창용마을무리의개수.txt")

tc=int(input())
for i in range(tc):
    n,m=map(int, input().split())
    graph=[[] for _ in range(n+1)]
    visit=[False for _ in range(n+1)]
    
    for _ in range(m):
        x,y=map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)
        
    def dfs(s):
        visit[s]=True
        for i in graph[s]:
            if visit[i] == False:
                dfs(i)
    cnt=0
    for j in range(1,n+1):
        if visit[j] == False:
            cnt+=1
            dfs(j)
        
    print(f'#{i+1} {cnt}')