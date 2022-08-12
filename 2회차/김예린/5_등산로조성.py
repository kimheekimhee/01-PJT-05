import sys

t = int(input())
for test_case in range(1, t + 1):

    dx = [0, 0, 1, -1]	# 우 좌 하 상
    dy = [1, -1, 0, 0]


    n, k = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(n)]
    visit = [[False] * n for _ in range(n)]

    trail = []
    for i in range(n):
        for j in range(n):
            if maps[i][j] == max(maps) and not visit[i][j]:
                maps(i, j)
                trail.append(cnt)

        stack = []
        stack.append((i, j))
        visit[i][j] = True
        cnt = 0                            # 등산로 길이                  
        
        while stack:
            x, y = stack.pop()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < n and not visit[nx][ny]:
                    if maps[nx][ny] < maps[x][y]:
                        cnt += 1
                        visit[nx][ny] = True
                        stack.append((nx, ny))

    print(max(trail))


sys.stdin = open("_등산로조성.txt")
