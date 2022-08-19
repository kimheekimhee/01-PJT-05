import sys
from pprint import pprint

sys.stdin = open("_등산로조성.txt")

T = int(input())
for _ in range(1, T + 1):
    N, K = map(int, input().split())
    real_map = [list(map(int, input().split())) for a in range(N)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    stack = []
    max_ = []
    for d in range(K + 1):
        for e in range(N):
            for f in range(N):
                distances = [[0] * N for i in range(N)]
                maps = []
                for s in range(N):
                    part = []
                    for v in range(N):
                        part.append(real_map[s][v])
                    maps.append(part)
                cnt = 0
                maps[e][f] -= d
                heights = []
                for b in range(N):
                    heights.append(max(maps[b]))
                highest = max(heights)
                for h in range(N):
                    cnt += maps[h].count(highest)
                if cnt <= 5:
                    for x in range(N):
                        for y in range(N):
                            if maps[x][y] == highest:
                                stack.append((x, y))
                                while len(stack) != 0:
                                    cur = stack.pop()
                                    for c in range(4):
                                        mx = cur[0] + dx[c]
                                        my = cur[1] + dy[c]
                                        if 0 <= mx < N and 0 <= my < N and maps[cur[0]][cur[1]] > maps[mx][my]:
                                            stack.append((mx, my))
                                            if distances[mx][my] < distances[cur[0]][cur[1]] + 1:
                                                distances[mx][my] = distances[cur[0]][cur[1]] + 1
                    for g in range(N):
                        max_.append(max(distances[g]))

    print(f'#{_} {max(max_) + 1}')
    # 출력은 정상이지만 문제제출 시 51개의 테스트케이스중 한개만 틀렸다고 나온다.
    # 이유를 모르겠다.