import sys

sys.stdin = open("/Users/yuyeong/Desktop/알고리즘/01-PJT-05/1회차/김유영/_등산로조성.txt")

# 델타 탐색
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(start, skill, count):
    x = start[0]
    y = start[1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 범위 밖으로 나가지 않기
        
t = int(input())
n, k = map(int, input().split())
mountain = []
max_h = 0

