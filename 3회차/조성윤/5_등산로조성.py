from pprint import pprint
import sys

sys.stdin = open("_등산로조성.txt")

delta = ((-1, 0), (1, 0), (0, -1), (0, 1))


def DFS_construction(r, c, h, limit, length, n, k, area, visited) :
    global max_length
    visited[r][c] = 1 # 방문

    if max_length < length :
        max_length = length
    
    for dr, dc in delta :
        nr, nc = r + dr, c + dc # 다음 위치
        if 0 <= nr < n and 0 <= nc < n : # 범위 체크
            nh = area[nr][nc] # 다음 위치의 높이
            if visited[nr][nc] == 0 : # 다음 위치의 방문 여부 체크
                if nh < h : # 다음 위치의 원래 높이가 기존 위치의 높이보다 낮음 
                    DFS_construction(nr, nc, nh, 1, length+1, n, k, area, visited) # 다음 위치 좌표 및 높이, 공사 안 함, 길이 증가
                elif nh >= h and limit != 0 : # 다음 위치의 원래 높이가 기존 위치보다 높거나 같고 공사 아직 안 함
                    for i in range(1, k+1) :
                        nh -= i # 다음 위치의 높이를 정수 단위로 깎아나감
                        if nh < h : # 깎은 높이가 기존 높이보다 낮아지면
                            break # 반복문 탈출
                    DFS_construction(nr, nc, nh, 0, length+1, n, k, area, visited) # 다음 위치 좌표 및 높이, 공사 안 함, 길이 증가   
    
    visited[r][c] = 0 # 끝자락에 도달했으면 백트래킹하면서 방문 해제

    # stack = list()
    # stack.append((r, c, area[r][c], 1, 1)) # 처음 좌표 (r, c), 처음 좌표 높이, 남은 공사 횟수, 현재 등산로 길이
    # while stack :
    #     pr, pc, ph, plimit, plength = stack.pop()
    #     if visited_list[pr][pc] == 0 : # 방문 여부 체크
    #         visited_list[pr][pc] = 1
    #     for dr, dc in delta :
    #         nr, nc = pr + dr, pc + dc # 다음 위치
    #         if 0 <= nr < n and 0 <= nc < n : # 범위 체크
    #             nh = area[nr][nc] # 다음 위치의 높이
    #             if visited_list[nr][nc] == 0 : # 다음 위치의 방문 여부 체크
    #                 if nh < ph : # 다음 위치의 원래 높이가 기존 위치의 높이보다 낮음 
    #                     stack.append((nr, nc, nh, plimit, plength+1)) # 다음 위치 좌표, 공사 안 함, 길이 증가
    #                 elif nh >= ph and plimit != 0 : # 다음 위치의 원래 높이가 기존 위치보다 높거나 같고 공사 아직 안 함
    #                     for i in range(1, k+1) :
    #                         nh -= i # 다음 위치의 높이를 정수 단위로 깎아나감
    #                         if nh < ph : # 깎은 높이가 기존 높이보다 낮아지면
    #                             stack.append((nr, nc, nh, plimit-1, plength+1)) # 깎았던 다음 위치 좌표, 공사했음, 길이 증가
        
    #     # print(stack)
    #     # print(pr, pc, ph, plimit, plength)
    #     # pprint(visited_list)
    #     if max_length < plength : # 가장 긴 길이 갱신
    #         max_length = plength  

    # return max_length
                    

T = int(input())
for test_case in range(1, T+1) :
    N, K = map(int, input().split())
    mountain = [list(map(int, input().split())) for _ in range(N)]
    visited_list = [[0 for _ in range(N)] for _ in range(N)]
    high_len = max(map(max, mountain))
    max_length = 0
    for i in range(N) :
        for j in range(N) :
            if mountain[i][j] == high_len :
                DFS_construction(i, j, mountain[i][j], 1, 1, N, K, mountain, visited_list)

    print(max_length)
