import sys
sys.stdin = open("_등산로조성.txt")
# from pprint import pprint

T = int(input())

def dfs(x, y):
    global max_trail, touch

    # 4방향 이동
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        # 범위 확인
        if not(0 <= nx < N and 0 <= ny < N):
            continue
        if visited[nx][ny] == 1:
            continue

        # 등산로 탐색
        if maps[x][y] > maps[nx][ny] and visited[nx][ny] == 0:
            visited[nx][ny] = visited[x][y] + 1
            dfs(nx, ny)
            # 등산로 최대값 측정
            if visited[nx][ny] > max_trail:
                    max_trail = visited[nx][ny]
            # 갔다 왔을 때 초기화
            visited[nx][ny] = 0
        
        # 봉우리 깎기 (딱 한 곳을 정해서 최대 K 깊이만큼 지형을 깎는 공사를 할 수 있다.)
        if maps[x][y] <= maps[nx][ny] and visited[nx][ny] == 0 and not touch:
            # 깎을 수 있는 범위 넣어서 확인
            for i in range(1, K+1):
                cut_height = maps[nx][ny] - i
                # 깎은 봉우리가 전 봉우리 높이보다 작아졌을 경우 다시 등산로 체크
                if cut_height < maps[x][y]:
                    maps[nx][ny] = cut_height
                    touch = True
                    # 등산로 체크 (위랑 같음)
                    visited[nx][ny] = visited[x][y] + 1
                    dfs(nx, ny)
                    if visited[nx][ny] > max_trail:
                        max_trail = visited[nx][ny]

                    # 원래대로 봉우리 복구
                    maps[nx][ny] = maps[nx][ny] + i
                    touch = False
                    visited[nx][ny] = 0


for tc in range(1, T+1):
    N, K = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(N)]

    max_trail = 0
    touch = False

    dy = [-1,0,1,0]
    dx = [0,1,0,-1]

    # 가장 높은 봉우리 좌표 구하기
    max_ = max(map(max,maps))
    max_peaks = []

    for i in range(N):
        for j in range(N):
            if maps[i][j] == max_:
                max_peaks.append((i, j))
    
    # 높은 봉우리 탐색 시작
    for d in max_peaks:
        # 시작 좌표 
        x, y = d
        visited = [[0] * N for _ in range(N)]
        # 높은 봉우리 표시 후 시작
        visited[x][y] = 1
        dfs(x, y)

    print(f'#{tc} {max_trail}')
    
