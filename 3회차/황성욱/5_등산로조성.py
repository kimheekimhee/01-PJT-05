from collections import deque
import sys
from pprint import pprint

sys.stdin = open("_등산로조성.txt")
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    que = deque()
    que.append([x, y])
    arr[x][y] = 1
    cnt = 0
    
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= n or ny >= n or nx < 0 or ny < 0:
                continue

            if matrix[nx][ny] >= matrix[x][y]:
                continue

            if matrix[nx][ny] < matrix[x][y]:
                arr[nx][ny] = arr[x][y] + 1
                que.append([nx, ny])
                cnt = max(cnt, arr[nx][ny])
                
    return cnt

t = int(input())
for i in range(t):
    n, dep = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    
    max_val = 0
    for j in range(n):
        for k in range(n):
            max_val = max(max_val, matrix[j][k])  # 최대 봉우리 높이
   
    res = 0
    for j in range(n):
        for k in range(n):
            if matrix[j][k] == max_val:           # matrix의 요소가 최대 봉우리라면
                for q in range(n):                # 최대 봉우리일 때를 제외한 모든 요소를 range(1, dep + 1) 빼준 후 
                    for p in range(n):                      
                        if q != j or p != k:
                            for d in range(1, dep + 1):
                                if matrix[q][p] - d >= 0:
                                    arr =[[0] * (n) for _ in range(n)]
                                    matrix[q][p] -= d
                                    res = max(res, bfs(j, k))            # bfs로 최대 값을 갱신
                                    matrix[q][p] += d                    # 빼준 값을 돌려줌
    print(f'#{i + 1}', res)


                