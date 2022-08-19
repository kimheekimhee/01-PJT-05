from collections import deque
import sys

sys.stdin = open("_등산로조성.txt")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n,k= map(int,input().split())


    mou=[list(map(int,input().split())) for __ in range(n)]


    dy=[1,-1,0,0]
    dx=[0,0,-1,1]

    def way(y,x):
        visit[y][x]=1
        stack=[]
        stack.append((y,x))
        cntls=[0]
        cnt=1
        while stack:
            sm= stack.pop()
            cnt+=1
            move=0
            for i in range(4):
                ny= sm[0]+dy[i]
                nx= sm[1]+dx[i]
                if 0>ny or ny>= n  or 0>nx or nx>= n :
                    continue
                if visit[ny][nx]==1:
                    continue
                if  mou[sm[0]][sm[1]] > mou[ny][nx]:  #visit[ny][nx]==0 and
                    visit[ny][nx]=1
                    stack.append((ny,nx))
                    move=1
            if move == 0:
                    ny= sm[0]+dy[i]
                    nx= sm[1]+dx[i]
                    for i in range(4):
                        if 0>ny or ny>= n  or 0>nx or nx>= n :
                            continue
                        if mou[sm[0]][sm[1]]>mou[ny][nx]-k:
                            cnt+1
                            cntls.append(cnt)
                            cnt-=2
                            break
                        else:
                            cntls.append(cnt)
                            cnt-=1
                    else:
                        cntls.append(cnt)
                        cnt-=1
            rm=max(cntls)
        return(rm)




    mm= 0
    for y in range(n):
        for x in range(n):
            if mou[y][x]>mm:
                mm= mou[y][x]

    result=[]

    for y in range(n):
        for x in range(n):
            if mou[y][x]==mm:
                visit=[[0]*n for __ in range(n)]
                res= way(y,x)
                result.append(res)

    print(max(result))