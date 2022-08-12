from pprint import pprint

import sys

sys.stdin = open("_등산로조성.txt")

# 그래프를 입력 받고 가장 높은 봉우리의 위치를 저장
# 가장 높은 봉우리에서 상,하,좌,우로 델타 탐색해서 본인보다 낮은 것들을 새로운 리스트에 추가
# --- 경로를 추가하고 싶었지만 실패하였습니다. ---
# 새로운 리스트들의 요소들을 활용해서 다시 한 번 델타 탐색, 각 요소별로 주변 값들을 -1부터 -k만큼 빼 준후 또 dfs 시행,
# 방문 횟수가 가장 큰 것을 남김
# 최대 방문 횟수 출력

# 테스트 케이스
T = int(input())
for test_case in range(1, T+1):
    # 지도 길이, 최대 공사 가능 입력
    N, K = map(int, input().split())

    # 지도 저장용 리스트 생성
    graph_ = []
    # 지도 입력 받음
    for _ in range(N):
        graph_.append(list(map(int, input().split())))
    #print(graph_)

    # 방문용 boolen 리스트 생성
    # bfs 돌릴 때마다 초기화를 해줘야 할 수 있을 듯
    visited= [[False] * N for _ in range(N)]
    #print(visited)

    # 가장 큰 값을 찾고
    max_ = 0
    for i in range(N):
        for j in range(N):
            if graph_[i][j] > max_:
                max_ = graph_[i][j]
    # print(max_)
    max_list = []
    # 가장 큰 값들의 인덱스를 저장
    for i in range(N):
        for j in range(N):
            if graph_[i][j] == max_:
                max_list.append([i,j])
    # print(max_list)

    # 델타 탐색용 리스트 생성
    # 상, 하, 좌, 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 높은 봉우리 중에서
    for high in max_list:
        # 경로 저장용 리스트 생성
        trail = []

        # 시작 좌표값 불러오기
        sx, sy = high[0], high[1]

        # 스택용 리스트 추가
        stack = [[sx, sy]]
        # 방문으로 처리
        visited[sx][sy] = True

        # 스택이 있는 동안
        while stack:
            # 현재 좌표를 stack에서 뽑아서 사용해야 함
            cur = stack.pop()

            # 현재 좌표를 기준으로 델타 탐색
            for d in range(4):
                nx = cur[0] + dx[d]
                ny = cur[1] + dy[d]
                
                # 새로운 좌표값이 범위를 벗어나지 않고, 현재 값보다 작고
                if (-1 < nx < N and -1 < ny < N) and graph_[nx][ny] < graph_[cur[0]][cur[1]]:
                    # 방문하지 않았다면 
                    if not visited[nx][ny]:
                        print(cur[0], cur[1], nx, ny)
                        print(graph_[cur[0]][cur[1]], graph_[nx][ny])
                        # 스택에 쌓고
                        stack.append([nx,ny])
                        # 방문 처리
                        visited[nx][ny] = True
                        pprint(visited)