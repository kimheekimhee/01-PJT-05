from re import L
import sys

sys.stdin = open("_Flatten.txt")


n, m = list(map(int, input().split()))
# 좌하 우 우하 좌 순으로 탐색
dx = [1, 0, 1, 0]
dy = [-1, 1, 1, -1]

# 빈 박스 테이블 생성
box_table = []

for _ in range(n):
    temp_list = list(map(int, input().split()))
    box_table.append(temp_list)

    # 이차원 리스트 순회
    for x in range(n):
        for y in range(m):
            
            # 델타 탐색
            for d in range(4):
                flatten = 0
                nx = x + dx[d]
                ny = y + dy[d]

                while True:
                    if not(-1 < nx < n and -1 < ny < n): # 범위에서 벗어나지 않으면
                        break
                    if box_table[x][y] != 0 or box_table[y][x] != 0:
                        break
                    
                    flatten += 1
                    # 가장 높은 곳과 낮은 곳의 차이가 1 이하면
                    if len(flatten) <= 1:
                        nx = x + dx[d]
                        ny = y + dy[d]

                        if not(-1 < nx < n and -1 < ny < n) or (box_table[x][y] != 0 or box_table[y][x] != 0):
                            
                            print(box_table[x][y], box_table[x][y])
                            print(x - 1, y - 1)
                            flatten = (box_table[x][y], box_table[x][y])
else:
    print(flatten)












