import sys

# sys.stdin = open("_등산로조성.txt")
sys.stdin = open("t.txt")

# 델타 탐색 문제인데 가로세로만 하면됨
# 일단 2차원 리스트를 순회 하면서 가장 높은 값을 찾고 
# 순회하면서 최대값과 같은 애는 바로 탐색 한번하고
# k 값을 적용 후 또 한번 탐색한다.
# 각 탐색이 이루어 질 때 마다 최대 길이를 기록할 수 있는 변수를 설정해서 
# 탐색 끝나고 최대값 변수를 출력하면 답이 될 듯 
# 시계방향으로 탐색을 해보자..

# 상 우 하 좌 왜 y를 먼 하는지 모르지만,, 수업에서 그랬으니 그냥 해봄#
dy=[-1,0,1,0]
dx=[0,1,0,-1]
# 델타 만듬..

T=int(input())
N,K = map(int,input().split())

for _ in range(T):
    mat = [list(map(int,input().split())) for _ in range(N)]
# print(mat)
    max_num = 0
    for i in range(N):
        for j in range(N):
            if mat[i][j] > max_num:
                max_num = mat[i][j] # 9 구했음
    long = 0
    for y in range(N):
        for x in range(N):
            if mat[y][x] == max_num:# 가장 큰 값을 찾았다면
                
                for d in range(4): # 델타 범위 지정
                    ny = y + dy[d]
                    nx = x + dx[d]

                    while 1:
                        if not (-1<ny<N and -1<nx<N): # 범위 안에 없으면
                            break
                        if mat[y][x] < mat[ny][nx]: # 현재 값보다 크면 
                            break
                
                        long += 1
                        ny = ny + dy[d]
                        nx = nx + dx[d]

                print(long)



    # print(max_num)


