import sys
from collections import deque

sys.stdin = open("_등산로조성.txt")

T = int(input())

def bfs(x, y):
    global K, board, highest

    visited = [[False] * N for _ in range(N)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque()
    q.append((1, x, y))
    d_list = []
    # K 만큼 깎은 횟수이다.
    flag = False

    while q:
        d, i, j = q.popleft()

        if not visited[i][j]:
            visited[i][j] = True

            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]

                if -1 < nx < N and -1 < ny < N:
                    if not visited[nx][ny]:
                        if board[i][j] > board[nx][ny]:
                            print(f"{x}, {y} :", d + 1, nx, ny)
                            q.append((d + 1, nx, ny))
                        elif board[i][j] > board[nx][ny] - K and not flag:
                            flag = True
                            print(f"{x}, {y} :", d + 1, nx, ny)
                            q.append((d + 1, nx, ny))
                        else:
                            d_list.append(d)
                    else:
                        d_list.append(d)

    return max(d_list) if d_list else 0


for i in range(1, T + 1):
    N, K = map(int, input().split())

    board = []
    highest = -1

    for j in range(N):
        line = list(map(int, input().split()))
        highest = max(line) if highest < max(line) else highest
        board.append(line)

    start = [(j, k) for j in range(N) for k in range(N) if board[j][k] == highest]

    ret = []

    for x, y in start:
        ret.append(bfs(x, y))

    print(f"#{i}", ret)