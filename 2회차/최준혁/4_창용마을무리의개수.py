# sys.stdin = open("_창용마을무리의개수.txt")
import sys
sys.setrecursionlimit(10**7) # 재귀 제한
T = int(input()) # 테스트케이스 
input = sys.stdin.readline 

for t in range(1, T+1):
    N, M = map(int, input().split()) # N명의 사람,  M 개의 줄
    adj_list = [[] for _ in range(N+1)] # 창용마을 사람이 1번부터 N번까지 이므로 N+1
    visited = [False] * (N + 1) # 방문 판별하기
    answer = 0 # 무리의 수 카운트

    def dfs(n): # dfs(1)
        visited[n] = True # visited[1] = True 
        for i in adj_list[n]: # adj_list[1] 확인 -> [2, 5]
            if visited[i] == False: # if visited[2] == False
                visited[i] = True # visited[2] = True
                dfs(i) # dfs(2) 재귀


    for i in range(M): # 인접 리스트 생성
        u, v = map(int, input().split()) # 6 5 / 1 2 / 2 5 ... 
        adj_list[u].append(v) # adj_list[6].append(5)
        adj_list[v].append(u) # adj_list[5].append(6)..
    # [[], [2, 5], [1, 5], [4], [3, 6], [2, 1], [4]]
    
    for number in range(1, N+1): # 1 2 3 4 5 6
        # print(number)
        if not visited[number]: # 방문하지 않은 곳이 있으면 ex) visited[1]
            visited[number] = True # True visited[1] = True
            answer += 1 # answer = 1 
            dfs(number) # 함수 호출  dfs(1)

    
    print("#{} {}".format(t, answer))