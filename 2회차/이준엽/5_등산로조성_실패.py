import sys

sys.stdin = open("_등산로조성.txt")

t = int(input())
delta = [(-1,0),(1,0),(0,-1),(0,1)]
for _ in range(1,t+1):
    n,m = map(int,input().split())
    maps = [list(map(int,input().split())) for i in range(n)]
    full_paths = []

    for i in range(n):
        for j in range(n):
            max_paths = []

            maxheight = max(list(max(maps[i]) for i in range(n)))
            if 
