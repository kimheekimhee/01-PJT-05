from pprint import pprint
import sys
def dfs(x, y):
    visited = [[0] * N for _ in range(N)]
    visited[x][y] = 1
    start = [(x, y)]
    cut = False
    while start:
        a, b = start.pop()
        for k in range(4):
            nx, ny = a + dx[k], b + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                if matrix[nx][ny] - K <= matrix[a][b] and not cut and visited[nx][ny] == 0:
                    visited[nx][ny] = visited[a][b] + 1
                    cut = True
                    start.append((nx, ny))
                elif matrix[nx][ny] < matrix[a][b] and visited[nx][ny] == 0:
                    visited[nx][ny] = visited[a][b] + 1
                    start.append((nx, ny))
    return cut
sys.stdin = open("_등산로조성.txt")
T = int(input())
for i in range(1, T+1):
    N, K = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    dx, dy = [0, 1, 0, -1],[1, 0, -1, 0] # 우 하 좌 상
    result = []
    cut = False
    ma = max(map(max, matrix))
    rere = []
    for x in range(N):
        for y in range(N):
            if matrix[x][y] == ma:
                result.append((x,y))
    for k in result:
        a, b = k
        rere.append(dfs(a, b))
    pprint(rere)