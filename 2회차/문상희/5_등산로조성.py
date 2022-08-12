import sys

sys.stdin = open("_등산로조성.txt")
from collections import deque

test_case = int(input())
for test in range(1, test_case + 1):
    size, depth = list(map(int, input().split()))
    maps = []
    check = []
    highest = 0
    h_p = []
    for i in range(size):
        line = list(map(int, input().split()))
        maps.append(line)
        hang = []
        for j in range(size):
            hang.append(0)
            if maps[i][j] > highest:
                highest = maps[i][j]
                h_p = []
                h_p.append([i, j])
            elif maps[i][j] == highest:
                h_p.append([i, j])
        check.append(hang)
    for i in h_p:
        check[i[0]][i[1]] = 1

    di = [1, -1, 0, 0]
    dj = [0, 0, -1, 1]

    def dfs(x, y, cut):
        stack = list()
        stack.append((x, y))
        maximum = 0
        if cut == 0:
            maps[x][y] -= depth
        while stack:
            a, b = stack.pop()
            for i in range(4):
                ni = a + di[i]
                nj = b + dj[i]
                if ni in range(size) and nj in range(size):
                    if maps[ni][nj] < maps[a][b]:
                        if check[ni][nj] <= check[a][b]:
                            stack.append((ni, nj))
                            check[ni][nj] = check[a][b] + 1
                            if check[ni][nj] > maximum:
                                maximum = check[ni][nj]

                    elif maps[ni][nj] - depth < maps[a][b]:
                        if cut == 1:
                            cut -= 1
                            stack2 = list()
                            stack2.append((ni, nj))
                            maps[ni][nj] -= depth
                            while stack2:
                                a2, b2 = stack2.pop()
                                for j in range(4):
                                    ni2 = a2 + di[j]
                                    nj2 = b2 + dj[j]
                                    if ni2 in range(size) and nj2 in range(size):
                                        if maps[ni2][nj2] < maps[a2][b2]:
                                            if check[ni2][nj2] <= check[a2][b2]:
                                                stack2.append((ni2, nj2))
                                                check[ni2][nj2] = check[a2][b2] + 1
                                                if check[ni2][nj2] > maximum:
                                                    maximum = check[ni2][nj2]
                            maps[ni][nj] += depth
        return maximum
    
    long = []
    for p in h_p:
        i, j = p
        if check[i][j] == 1:
            x = dfs(i, j, 1)
            long.append(x)
            for i2 in range(size):
                for j2 in range(size):
                    if maps[i2][j2] == highest:
                        check[i2][j2] = 1
                    else:
                        check[i2][j2] = 0
    print(long)
    # print(f'#{test} {max(long)}')