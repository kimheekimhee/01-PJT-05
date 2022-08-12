
import sys

sys.stdin = open("_창용마을무리의개수.txt")



T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n,m= map(int,input().split())

    node=[[] for __ in range(n+1)]

    visit=[False]*(n+1)

    def vi(i):
        stack=[]
        stack.append(i)
        visit[i]=True
        while stack:
            s = stack.pop()
            for k in node[s]:
                if visit[k]==True:
                    continue
                if visit[k]==False:
                    visit[k]=True
                    stack.append(k)

    for __ in range(m):
        u,v = map(int,input().split())
        node[u].append(v)
        node[v].append(u)

    cnt=0
    for j in range(1,n+1):
        if visit[j]==True:
            continue
        if visit[j]==False:
            vi(j)
            cnt+=1

    print(f'#{test_case} {cnt}')