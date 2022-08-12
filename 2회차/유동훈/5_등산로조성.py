import sys

sys.stdin = open("_등산로조성.txt")

# T = int(input())
# for i in range(1, T+1):
#     map_ = []
#     N, K = map(int, input().split())
#     for _ in range(N):
#         map_.append(input().split())

#     dx = [0, 0, -1, 1]
#     dy = [1, -1, 0, 0]

#     for j in range(N):
#         for k in range(N):
#             if map_[j][k] == max(max(map_)):
#                 for l in range(4):
#                     map_[j+dx[l]][k+dy[l]] > map_

N = 5

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
cnt = 0
visited = [0]*N

def move(graph, x, y, visited):
    for _ in range(4):
        if graph[x][y] > graph[x+dx][y+dy]:
            cnt += 1
            x += dx
            y += dy
        move(graph, x, y visited)
