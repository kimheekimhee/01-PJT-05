import sys
from pprint import pprint
sys.stdin = open("_등산로조성.txt")

T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    
    road_map = []
    
    for _ in range(N):
        road_map.append([*map(int, input().split())])
    
    highest = max(road_map[0])
    h_list = []
    
    for y in range(N):
        for x in range(N):
            if road_map[y][x] > highest:
                highest = road_map[y][x]
                h_list = []
                h_list.append([y, x])
            elif road_map[y][x] == highest:
                h_list.append([y, x])
    
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    
    road = []
    visited = []
    
    for _ in range(N):
        visited.append([False] * N)
        
    for road_map_hyhx in h_list:
        
        visited[road_map_hyhx[0]][road_map_hyhx[1]] = True
        stack = [road_map_hyhx[road_map_hyhx[0]][road_map_hyhx[1]]]
        current = stack.pop(0)
        
        while stack:
            
            if not visited[current[0]][current[1]]:
                stack.append()
        
        if -1 < ny < N and -1 < nx < N and :
            if road_map[ny][nx] > road_map[ny + dy[i]][nx + dx[i]]:
                if not visited[ny][nx]:
                    
        for i in range(4):
            ny = road_map_hyhx[0] + dy[i]
            nx = road_map_hyhx[1] + dx[i]
            if -1 < ny < N and -1 < nx < N:
                if road_map[ny][nx] > road_map[ny + dy[i]][nx + dx[i]]:
                    if not visited[ny][nx]:
                        visited[ny][nx] = True
                        ny = ny + dy[i]
                        nx = nx + dx[i]