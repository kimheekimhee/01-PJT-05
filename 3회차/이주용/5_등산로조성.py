import sys
from collections import deque
from pprint import pprint

def dfs(x, y, n, land, visited, length):
    visited[x][y] = True
    length[x][y] = 1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    stack = [[x, y]]
    while stack:
        trial = 1
        v = stack.pop()
        vx = v[0]
        vy = v[1]
        print(v)
        construction = []
        construction_position = 0
            
        # 공사 취소
        if v == construction:
            trial = 1
            land[vx][vy] = construction_position
            
        stack_length_1 = len(stack)
        for d in range(4):
            nx = vx + dx[d]
            ny = vy + dy[d]
            # 새 좌표가 범위 내에 있고 고도차가 있으며
            if 0 <= nx < n and 0 <= ny < n and land[nx][ny] < land[vx][vy]:
                # 개척이 되지 않았다
                if visited[nx][ny] == False:
                    length[nx][ny] = length[vx][vy] + 1
                    stack.append([nx, ny])
                # 개척이 되긴 되었는데 바로 전에 방문한 좌표가 아니며 더 긴 루트를 개척할 수 있다
                elif visited[nx][ny] == True and length[nx][ny] != length[vx][vy] + 1 and length[vx][vy] + 1 > length[nx][ny]:
                    length[nx][ny] = length[vx][vy] + 1
                    stack.append([nx, ny])
            # 새 좌표가 범위 내에 있으나 더 높은 곳이며
            if 0 <= nx < n and 0 <= ny < n and land[nx][ny] >= land[vx][vy]:
                # 공사 가능하며 공사로 이전 위치보다 낮출 수 있다
                if trial == 1 and land[nx][ny] - k < land[vx][vy]:
                    # 원래 높이 정보를 저장하고
                    construction = [nx, ny]
                    construction_position = land[nx][ny]
                    # 공사한다
                    land[nx][ny] = land[vx][vy] - 1
                    length[nx][ny] = length[vx][vy] + 1
                    visited[nx][ny] = True
                    stack.append([nx, ny])
        stack_length_2 = len(stack)
        # 스택에 채워진 것이 아무것도 없다 : 탐색이 끝났다
        if stack_length_1 == stack_length_2:
            condition = True
        else:
            condition = False
        if condition == True:
            visited[stack[-1][0]][stack[-1][1]] = False
            
            
            
    max_length = 0
    for a in range(n):
        for b in range(n):
            if length[a][b] > max_length:
                max_length = length[a][b]
    return max_length    

sys.stdin = open("_등산로조성.txt")
# 가장 높은 봉우리에서 시작
# 높은 곳에서 낮은 곳으로, 상하좌우만 연결
# 딱 한 곳을 최대 k만큼 높이를 줄일 수 있음, 높이가 1보다 작아지는 것도 가능
t = int(input())
for i in range(1, t + 1):
    n, k = map(int, input().split())
    land = [list(map(int, input().split())) for _ in range(n)]
    # 가장 높은 곳의 높이를 찾기
    max_height = 0
    for a in range(n):
        for b in range(n):
            if land[a][b] > max_height:
                max_height = land[a][b]
                
    # 가장 높은 곳의 좌표를 찾기
    max_height_list = []
    for a in range(n):
        for b in range(n):
            if land[a][b] == max_height:
                max_height_list.append([a, b])
                
    # 등산로 길이의 모든 경우의 수 넣기
    route_list = []
    visited = [[False] * n for _ in range(n)]
    length = [[0] * n for _ in range(n)]
    
    
    for start in max_height_list:
        route_list.append(dfs(start[0], start[1], n, land, visited, length))
    print(route_list)
    
            

    
   

                    
                        
        
        
    
    