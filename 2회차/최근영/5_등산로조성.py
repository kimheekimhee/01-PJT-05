import sys

sys.stdin = open("_등산로조성.txt")

T = int(sys.stdin.readline())

dx = [0, 1, 0, -1]
dy = [-1,0, 1, 0]

for i in range(1,2):
    total_road = []
    N,K = list(map(int,sys.stdin.readline().split()))
    matrix = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
    compare_ = 0
    # 매트릭스 내의 최대 값 찾기 == 봉우리 찾는 것
    for j in range(len(matrix)):
        for k in range(len(matrix)):
            if matrix[j][k] > compare_:
                compare_ = matrix[j][k] # 찾은 맥스 값을 compare_ 변수에 저장
    
    for j in range(len(matrix)-1):
        for k in range(len(matrix)-1):
            if matrix[j][k] == compare_: # 매트릭스에서 맥스값과 같을때
                build_cnt = 0
                build_list = []
                road=[compare_]
                max_val = 0
                max_val_same = 0
                compare_list = []
                while True:
                    for l in range(len(dx)): # 상하좌우 탐색
                        x = k + dx[l]
                        y = j + dy[l]
                        if 0 <= x <= N-1 and 0 <= y <= N-1: # 범위를 넘지 않을때
                            print('넘음')
                            if matrix[j][k] > matrix[x][y]:
                                if matrix[x][y] > max_val:
                                    max_val = matrix[x][y]
                                    index_list = list([x,y])
                    k = index_list[0]
                    y = index_list[1]
                    print(max_val)
                        # elif matrix[j][k] == matrix[x][y] and build_cnt == 0:
                            # for p in range(1,K+1):
                                # compare_list.append(matrix[x][y] - p)
                            # build_cnt += 1
                            # build_list = [x,y]
                # if not compare_list:
                    # for q in compare_list:
                        # if q > max_val and q < matrix[j][k]:
                            # max_val = q
                # else:
                    # continue
                # road.append(max_val)
                # if val_list.count(max(val_list)) >= 2:
                    # com = 0
                    # index_list_2 = []
                    # for l in val_list:
                        # if l == max(val_list): # l이 맥스 값일때 x,y 좌표 반환
                            # j = index_list[val_list.index(l)][0]
                            # k = index_list[val_list.index(l)][1]
                            # for l in range(len(dx)):
                                # x = j + dx[l]
                                # y = j + dy[l]
                                # if 0 < x <= N-1 and 0 < y <= N-1: # 범위를 넘지 않을때
                                    # 
                # elif val_list.count(max(val_list)) == 1:
                    # for l in val_list: # 값리스트 값들 중
                        # if l == max(val_list): # l이 맥스 값일때 x,y 좌표 반환
                            # j = index_list[val_list.index(l)][0]
                            # k = index_list[val_list.index(l)][1]
                    # if len(val_list) == 0:
                        # total_road.append(road)
                        # break