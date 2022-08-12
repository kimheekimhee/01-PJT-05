import sys

sys.stdin = open("_창용마을무리의개수.txt")

T = int(input())

# 아는 사이?  = 인접 리스트
for tc in range(1, T+1):
    N, M = map(int, input().split())
    
    graph = [ [] * N for _ in range(N+1)]

    for i in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    # 이 사람 아세요..?
    know = [False] * (N+1)
    
    # 우리끼리 친해요
    cnt = 0 
    
    # 정점을 증가시켜주는 반복문
    for i in range(1, N+1):
        
        # 방문하지 않았을 때만 dfs 진입 가능
        if know[i] == False:
            
            '''
            dfs 로직 = 스택에 넣고 >> True 변환 >> 스택 요소를 꺼내서 >> 인접 리스트 False 확인 >> False > True 변경 
            >> True 요소 스택에 추가(반복)
            '''
            
            def dfs(start):
                stack = [start]
                know[start] = True 
                
                while len(stack) != 0:
                    search = stack.pop()

                    for j in graph[search]:
                        if not know[j]:
                            know[j] = True
                            stack.append(j)
            dfs(i)                          # start에 들어갈 값을 증가시켜준다
            cnt += 1                        # 조직을 + 1
    
    print(f'#{tc} {cnt}')      
                    
'''
아직 dfs의 이해가 부족한 것 같습니다. 그래도 배운 것을 토대로 과정을 생각하면서 적어봤습니다
'''



    
    


