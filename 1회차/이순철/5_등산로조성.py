from pprint import pprint
import sys

sys.stdin = open("_등산로조성.txt")

t = int(input())
for t_case in range(1, t + 1):
    n, k = map(int, input().split())
    map_ = [list(map(int, input().split())) for _ in range(n)]
    # pprint(map_)
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    s_pt = []
    cnt = 0
    visit = [[False] * (n) for _ in range(n)]
    pprint(visit)
    # for sx in range(n):
    #     for sy in range(n):
    #         pt = map_[sx][sy]

    #         for i in range(4):
    #             nx = sx + dx[i]
    #             ny = sy + dy[i]
    #         if 0 <= nx <n and 0 <= ny <n:
    #             [nx][ny]
