import sys

sys.stdin = open("_등산로조성.txt")


dx=[1, -1, 0, 0]
dy=[0, 0, 1, -1]

def dfs(x, y, flag):
    global max_, visited
    max_=max(max_, visited[x][y])
    for a in range(4):
        nx = x+dx[a]
        ny = y+dy[a]
        if not (0 <= nx <n and 0 <= ny < n) or visited[nx][ny]:
            continue
        if map_[nx][ny] < map_[x][y]:
            visited[nx][ny] = visited[x][y]+1
            dfs(nx, ny, flag)
            visited[nx][ny]=0
        elif flag and map_[nx][ny] - k < map_[x][y]:
            temp = map_[nx][ny]
            map_[nx][ny] = map_[x][y]-1
            visited[nx][ny] = visited[x][y] + 1
            dfs(nx,ny,flag-1)
            visited[nx][ny] = 0
            map_[nx][ny] = temp
            
t = int(input())
for case in range(1, t+1):
    n, k = map(int, input().split())
    map_ = [list(map(int, input().split())) for _ in range(n)]
    hh = 0
    for i in range(n):
        for j in range(n):
            if map_[i][j]>hh:
                hh=map_[i][j]
    max_=0
    visited = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if map_[i][j] == hh:
                visited[i][j] = 1
                dfs(i,j,1)
                visited[i][j] = 0
    
    print(f'#{case} {max_}')