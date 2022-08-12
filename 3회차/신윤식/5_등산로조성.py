'''
못 풀겠습니다 ㅠㅠ
'''

import sys

sys.stdin = open("./3회차/신윤식/_등산로조성.txt")

dr = [0, 1, 0, -1] # 우 하 좌 상
dc = [1, 0, -1, 0] 

T = int(input())

for t in range(1, T+1):
    N, K = map(int,input().split())
    mountain = [list(map(int,input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    max_height = 0

    for row in range(N):
        for col in range(N):
            if mountain[row][col] > max_height:
                max_height = mountain[row][col]

    for row in range(N):
        for col in range(N):
            if mountain[row][col] == max_height:
                visited[row][col] = 1
                stack = [(row,col)]

                while stack:
                    cur_row, cur_col = stack.pop()

                    for i in range(4):
                        nr = cur_row + dr[i]
                        nc = cur_col + dc[i]

                        if 0 <= nr < N and 0 <= nc < N:
                            if visited[nr][nc] == 0:
                                visited[nr][nc] = 1
                                stack.append((nr,nc))

                   
