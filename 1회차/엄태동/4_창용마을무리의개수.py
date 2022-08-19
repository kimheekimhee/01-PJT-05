import sys

sys.stdin = open("_창용마을무리의개수.txt")
T=int(input())
for i in range(T):
    N,M=map(int, input().split())
    People=[[] for _ in range(N+1)]
    Group_num=0
    stack=[]
    visited=[False]*(N+1)
    visited[0]=True
    for j in range(M):
        a,b=map(int, input().split())
        People[a].append(b)
        People[b].append(a)   # ! 무방향이라는 것을 생각 안했음
    while 1:
        if visited.count(True)==N+1:  # 모두 visit 완료하면 while문 나감
            break
        for m in range(len(visited)): # visited 리스트에 False가 있으면 해당 인덱스로 접근
            if visited[m]==False: 
                start=m               # 해당 인덱스를 start로 선언
                stack.append(start) 
                visited[start]=True  
                if People[start]==[]:
                    stack=[]
                    Group_num+=1
                    continue
                while len(stack) != 0:
                    adj_graph=People[start]
                    for k in range(len(adj_graph)):     # 인접 그래프를 True로 만드는 과정
                        if visited[adj_graph[k]]==True: 
                            continue
                        visited[adj_graph[k]]=True 
                        stack.append(adj_graph[k]) 
                        # print(stack)
                        # print(visited)
                    start=stack.pop() 
                    # if visited[start]==True:
                    #     break
                # print(visited)
                stack=[]
                Group_num+=1
    print(f'#{i+1} {Group_num}')