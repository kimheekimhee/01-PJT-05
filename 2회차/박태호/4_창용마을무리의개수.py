import sys
sys.stdin = open("_창용마을무리의개수.txt")
# sys.stdin = open("t.txt")

#DFS문제같음 덩어리 문제
# 우선 입력 받고
# DFS구현 하는데
# 방문 하는 거 만들고 스택에 시작 pop 하고
# append하는거
# DFS가 실행이 되면 1 추가해야 덩어리 구함
# 와일문으로 조져보자 ㅇㅋ#

t = int(input())

for case in range(1,1+t):
    cnt = 0
    n,m = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    visit = [False] * (n+1) #방문
    # graph = [list(map(int,input().split()))]*(m+1)

    for _ in range(m):
        x,y = map(int,input().split())
        # print(x,y)
        graph[x].append(y)
        graph[y].append(x) # 그래프만듬

    # start = 1
    # visit[start] = True
    

    for s in range(1,len(visit)):
        # print(s)
        if visit[s] == False:
            # print('왔니')

            start = s
            cnt += 1
        # 
        stack = [start]

        while stack:
            # 현재값 
            cur = stack.pop()
            
            # print(cur)
            for i in graph[cur]:

                if not visit[i]: # 노방문이면
                    visit[i] = True
                    stack.append(i)
                     
        
                        # 구현함
            
    print(f'#{case} {cnt}')
    # print(graph)
    # print(visit)