import sys

sys.stdin = open("_등산로조성.txt")

"""
5 1
9 3 2 3 2
6 3 1 7 5
3 4 8 9 9
2 3 7 7 7
7 6 5 5 8
"""

def dfs(y, x, cnt, k):
    global res
    # cnt가 res보다 크면
    if res < cnt + 1:
        # res에 cnt + 1 저장
        res = cnt + 1

    # 방문 표시
    visited[y][x] = 1

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    # 4방위 탐색
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 탐색할 값이 배열 안에 있으면
        if -1 < nx < n and -1 < ny < n:
            # 방문하지 않았다면
            if visited[ny][nx] == 0:
                # 안 깎고 이동
                if arr[ny][nx] < arr[y][x]:
                    # dfs 탐색
                    dfs(ny, nx, cnt+1, k)
                
                # 깎고 이동
                elif arr[ny][nx] - k < arr[y][x]:
                    # 원래 값 잠깐 저장해놓기
                    tmp = arr[ny][nx]
                    # 깎기
                    arr[ny][nx] = arr[y][x] - 1
                    dfs(ny, nx, cnt+1, 0)
                    # 원래 값으로 되돌아옴
                    arr[ny][nx] = tmp
    
    visited[y][x] = 0

T = int(input())
for t in range(1, T+1):
    n, k = map(int, input().split())
    arr = []

    for i in range(n):
        arr.append(list(map(int, input().split())))

    visited = [[0] * n for _ in range(n)]
    res = 0
    max_ = 0

    # 배열에서 가장 큰 값 찾기
    for i in range(n):
        for j in range(n):
            if max_ < arr[i][j]:
                max_ = arr[i][j]

    list_ = []

    # 가장 큰값의 인덱스를 리스트에 저장
    for i in range(n):
        for j in range(n):
            if arr[i][j] == max_:
                list_.append([i, j])

    # 가장 큰값의 인덱스 y, x로 dfs 탐색
    for i in range(len(list_)):
        dfs(list_[i][0], list_[i][1], 0, k)

    print(f'#{t} {res}')