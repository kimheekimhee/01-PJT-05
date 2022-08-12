import sys

sys.stdin = open("_등산로조성.txt")

T = int(input()) # 테스트케이스 개수
# 상하좌우만 탐색
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def dfs(y, x, cnt, K, N):
    global result
    if(result < cnt + 1): # cnt + 1이 더 클 때 
        result = cnt + 1 # 결과 값에 넣어준다

    visited_list[y][x] = 1 # 1로 만들어준다.
    for i in range(4): # 탐색
        ny = y + dy[i]
        nx = x + dx[i]
        if (0 <= ny < N and 0 <= nx < N): # 범위내인지 확인
            if(visited_list[ny][nx] == 0):
                if (map_graph[ny][nx] < map_graph[y][x]): # 지금이 더크면
                    dfs(ny, nx, cnt+1, K, N) # 다시 dfs
                elif (map_graph[ny][nx] - K < map_graph[y][x]): # K만큼 깎았을때
                    temp = map_graph[ny][nx] #
                    map_graph[ny][nx] = map_graph[y][x] - 1
                    dfs(ny, nx, cnt+1, 0, N)
                    map_graph[ny][nx] = temp
    visited_list[y][x] = 0

for test_case in range(T):
    N, K = map(int, input().split()) # N: 한 변의 길이 , K: 최대 공사 가능 깊이
    map_graph = [list(map(int, input().split())) for _ in range(N)] # 지도 정보
    result = 0 # 결과값 저장할 변수
    max_height = max(max(map_graph)) # 지도에서 제일 높은 봉우리 크기
    max_height_list = [] # 제일 높은 봉우리들의 위치를 담을 리스트

    for i in range(N): # 전체 지도를 순회하면서
        for j in range(N):
            if map_graph[i][j] == max_height: # 제일높은 봉우리와 같으면 리스트에 위치를 담는다.
                max_height_list.append([i, j])

    visited_list= [[0] * N for i in range(N)] # 방문 체크할 리스트
    for i in range(len(max_height_list)): # 제일높은 봉우리들의 개수만큼 반복
        dfs(max_height_list[i][0], max_height_list[i][1], 0, K, N) # dfs 시작

    print(f'#{test_case+1} {result}') # 출력