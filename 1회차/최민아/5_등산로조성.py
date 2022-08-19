from re import X
import sys

sys.stdin = open("_등산로조성.txt")

delta = [(0, 1), (0, -1), (-1, 0), (1, 0)]  # 상하좌우 이동

def DFS(r, c):                              # 현재 위치를 받는 함수
    global visited                          # 방문 리스트
    
    for i in range(4):                      # 상하좌우 4가지로 이동 가능
        x, y = delta[i]                     # 델타 값
        nr, nc = r+x, c+y               # 이동했을 때 위치

        if not (0 <= nr < N and 0 <= nc < N) or visited[nr][nc]:
            continue                        # 부지를 벗어나거나 방문한 곳이면 건너뜀

        if high[r][c] > high[nr][nc]:       # 현재 위치보다 이동 위치 높이가 낮으면
            visited[nr][nc] = 1             # 이동 위치 방문 표시
            DFS(nr, nc)                     # 등산로 진행

        else:       # ??? 지형을 깎는 공사 구현 ???
            break   # ??? 등산로 길이 계산 방법 ???


T = int(input())                            # 테스트케이스 개수
for test_case in range(1, T+1):

    N, K = map(int, input().split())        # 부지 크기, 최대 공사 깊이
    high = [list(map(int, input().split())) for i in range(N)]
                                            # 봉우리 높이 지도
    top = 0
    for i in range(N):
        for j in range(N):
            if high[i][j] > top:
                top = high[i][j]            # 가장 높은 봉우리

    visited = [[0] * N for i in range(N)]   # 방문 확인
    road = 0                                # 등산로 길이

    for i in range(N):
        for j in range(N):
            if high[i][j] == top:           # 가장 높은 봉우리이면
                visited[i][j] = 1           # 방문 표시
                DFS(i, j)                   # 등산로 시작

    print(f'#{test_case} {road}')           # 최장 등산로 길이 출력