import sys

sys.stdin = open("_창용마을무리의개수.txt")


T = int(input())
N, M = map(int, input().split())
visited = [0] * (N + 1)
count = 0
for _ in range(1, T + 1):
    village = [[] for _ in range(N + 1)]

    for i in range(M):
        x, y = map(int, input().split())
        village[x].append(y)
        village[y].append(x)
        
# dfs 개념이 아직 부족해서 여기까지 밖에 못 풀었습니다.