import sys
from collections import deque

sys.stdin = open("_등산로조성.txt")

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(a, b):
    global answer

    q = deque()
    q.append((a, b, 1))

    while q:
        x, y, cnt = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                # 내가 가고자 하는 길이 나보다 낮으면 된다.
                if maps[nx][ny] < maps[x][y]:
                    q.append((nx, ny, cnt + 1))
        answer = max(answer, cnt)
def Mx_find(n, mx):
    for i in range(n):
        for j in range(n):
            if maps[i][j] == mx:
                start.append((i, j))

def fix(n, k):
    for i in range(n):
        for j in range(n):
            # 1 ~ k + 1 까지 공사가 가능하다고 했고 딱 한번만 가능하다고 했으니 한개씩 다 돌아 찾으면 되는것이다.
            for fix in range(k + 1):
                maps[i][j] -= fix
                # 스타트 지점 기준으로 다 돌아봐요
                for a, b in start:
                    bfs(a, b)
                # 다시 원상 복구!
                maps[i][j] += fix
for test_case in range(1, int(input()) + 1):
    n, k = map(int, input().split())
    maps, start = [], []
    mx, answer = 0, 0

    # 맵을 받으면서 최댓값을 찾는 과정이다.
    for i in range(n):
        lst = list(map(int, input().split()))
        mx = max(mx, max(lst))
        maps.append(lst)

    # mx_find 함수는 가장 높은 봉우리가 스타트 지점. 스타트지점을 start 리스트에 넣기 위함이다.
    mx_find(n, mx)
    # 공사을 했을때 등산로의 길이를 구하기 위한 함수
    fix(n, k)
    print(f"#{test_case} {answer}")