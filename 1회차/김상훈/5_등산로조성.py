import sys

sys.stdin = open("_등산로조성.txt")
from pprint import pprint

dx = [-1,0,1,0]
dy = [0,1,0,-1]
def dfs(x,y,dig):
    global max_load
    max_load = max(max_load, visited[x][y])
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if not (0 <= nx < N and 0 <= ny < N) or visited[nx][ny]:
            continue
        if mountain[x][y] > mountain[nx][ny]:
            visited[nx][ny] = visited[x][y] + 1
            dfs(nx, ny, dig)
            visited[nx][ny] = 0    
        elif dig and mountain[nx][ny] - K < mountain[x][y]:
            temp = mountain[nx][ny]
            mountain[nx][ny] = mountain[x][y] - 1
            visited[nx][ny] = visited[x][y] + 1
            dfs(nx, ny, dig-1)
            visited[nx][ny] = 0
            mountain[nx][ny] = temp
            
T = int(input())
for _ in range(1,T+1):
    
    N,K = map(int,input().split())
    # --------------------------------------------------
    mountain = []
    max_cf = 0
    for i in range(N):
        mountain.append(list(map(int,input().split())))
        for j in range(N):
            if mountain[i][j] > max_cf:
                max_cf = mountain[i][j]
                #-------------------------------------- 인접 행렬 생성 후 탐색하여 최댓값 저장.
    max_load = 0
    visited = [[False] * N for _ in range(N)] # 방문여부 확인하기 위한 visited
    
    for i in range(N):
        for j in range(N):
            if mountain[i][j] == max_cf: 
                visited[i][j] = True
                dfs(i,j,1)     # 최댓값에 대한 i , j dfs 탐색
                visited[i][j] = 0 
    print(f"#{_} {max_load}")
                
