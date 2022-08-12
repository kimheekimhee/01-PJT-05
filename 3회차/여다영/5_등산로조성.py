import sys
from pprint import pprint

sys.stdin = open("_등산로조성.txt")

T = int(input())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for _ in range(1, T + 1):
    N, K = map(int, input().split())
    matrix = [list(map(int, input().split())) for i in range(N)]

    top_height = 0
    for i in range(N):
        for j in range(N):
            if matrix[i][j] > top_height:
                top_height = matrix[i][j]

    #가장 높은 높이의 좌표들을 top_heights에 저장
    top_heights = []
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == top_height:
                top_heights.append([i, j])
    print(top_heights)

    #각 높이들에서의 paths들을 모두 저장
    #길을 탐색할 때, stack을 써야할 것 같은데?
    #not_visited & height이 더 작으면 이동
    for height in top_heights: