import sys

sys.stdin = open("_등산로조성.txt")

from pprint import pprint

T = int(input())
N, K = map(int, input().split())
road = []
for _ in range(N):
    road.append(list(map(int, input().split())))
pprint(road)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 이중리스트를 순회하는 반복문
for r in range(N):
    for c in range(N):
        
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            
            """
            델타탐색 범위에 더 작은 값이 있으면 해당 값으로 이동하고 싶었는데
            구현 실패 
            """
            if 0 <= nr <= N - 1 and 0 <= nc <= N - 1:
                if road[r][c] < road[nr][nc]:
                    print(nr, nc, road[nr][nc], d)
                    nr = nr + dr[d]
                    nc = nc + dc[d]
                    print("=======================")
                    print(nr, nc, road[nr][nc], d)