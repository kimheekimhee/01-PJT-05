import sys

sys.stdin = open("_등산로조성.txt")

for t in range(1, int(input())):
    m, k = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(m)]
    
    # 최소 mn, 최대 mx
    mn, mx = 20, 1
    mn_x, mn_y, mx_x, mx_y = 0, 0, 0, 0
    for i in range(m):
        for j in range(m):
            if board[i][j] < mn:
                mn = board[i][j]
                i, j = mn_x, mn_y
            if board[i][j] > mx:
                mx = board[i][j]
                i, j = mx_x, mx_y

    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]
    while True:
        board[mn_x][mn_y]
        leng = 1
         
    