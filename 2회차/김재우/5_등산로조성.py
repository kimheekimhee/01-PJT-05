import sys

sys.stdin = open("_등산로조성.txt")

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())    #지도 크기, 공사 가능 깊이
    
    mtn = [list(map(int, input().split())) for _ in range(N)] # 지도
    num_list = []
    
    # maximum = 
        # 상 하 좌 우
    nx = [0,0,-1,1]
    ny = [-1,1,0,0]

    for i in range(N):
        for j in range(N):
            num_list.append(mtn[i][j])

    for x in range(N):
        for y in range(N):
            if -1 > nx > N and -1 > ny > N:         # 조건문 이게 맞나..?
                if mtn[x][y] == max(num_list):       # 제일 높은 봉우리일때 탐색 시작
                    nx = x + nx[x]
                    ny = y + ny[y]




'''
    N * N 최대한 긴 등산로
    숫자는 지형의 높이
    조건 1. 가장 높은 숫자 시작(봉우리)
    조건 2. 가로, 세로 낮은 숫자로 가야한다.
    조건 3. 딱 한 곳 K만큼 줄일 수 있다.
'''
