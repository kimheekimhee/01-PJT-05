import sys

sys.stdin = open("_창용마을무리의개수.txt")

t = int(input())
for _ in range(1,t+1):
    n,m = map(int,input().split())
    relation = [[] for i in range(n+1)]
    visited = [False for i in range(n+1)]
    stack = []
    cnt = 0
    for i in range(m):
        a,b = map(int,input().split())
        relation[a].append(b)
        relation[b].append(a)


    for j in range(1,n+1):
        if visited[j] == False:
            stack.append(j)
            visited[j] = True 
            while stack:
                start = stack.pop()  
                for num in relation[start]:
                    if visited[num] == False:
                        stack.append(num)
                        visited[num] = True
            cnt+=1
    print(f'#{_} {cnt}')