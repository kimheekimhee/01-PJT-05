import sys
# from pprint import pprint
sys.stdin = open("_등산로조성.txt")

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, k, k_used, cnt):
    global max_walk
    visited[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
            if graph[x][y] > graph[nx][ny]:
                dfs(nx, ny, k, k_used, cnt + 1)

            elif graph[x][y] > graph[nx][ny] - k and k_used == False:
                temp = graph[nx][ny]
                graph[nx][ny] = graph[x][y] - 1 #가능한 적게 파기
                k_used = True
                dfs(nx, ny, k, k_used, cnt + 1)
                graph[nx][ny] = temp
                k_used = False

    if max_walk < cnt:
        max_walk = cnt

    visited[x][y] = 0 #다음 탐색을 위해 방문처리 초기화


T = int(input())
for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]

    temp = [] #최고점 구하기
    for i in range(n):
        temp.append(max(graph[i]))
    top = max(temp)
    
    start_point = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] == top: #최고점일때만 탐색하도록 탐색 좌표 저장
                start_point.append([i, j])

    visited = [[0] * n for _ in range(n)]
    walk_len = []

    for a, b in start_point: #최고점(a,b) top개의 최고산책로 저장
        k_used = False
        cnt = 1
        max_walk = 0
        dfs(a, b, k, k_used, cnt)
        walk_len.append(max_walk)
    print(f'#{test_case} {max(walk_len)}')