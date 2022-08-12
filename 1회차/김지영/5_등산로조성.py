# 등산로 조성
# 부지 N*N
# 최대한 긴 등산로
# 배열의 숫자는 지형의 높이
# 조건.
# 1. 등산로 시작 = 가장 높은 봉우리
# 2. 높은지형->낮은지형으로 가로,세로 방향 연결
# 3. 딱 한곳을 정해 최대 k깊이만큼 지형 깎을수있다..

# 입력의 맨 첫 줄에는 총 테스트 케이스의 개수 T가 주어지고, 
# 그 다음 줄부터 T개의 테스트 케이스가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 지도의 한 변의 길이 N, 
# 최대 공사 가능 깊이 K가 차례로 주어진다.
# 그 다음 N개의 줄에는 N * N 크기의 지도 정보가 주어진다.
import sys
def pprint(list):
    for i in list:
        print(i)
sys.stdin = open("_등산로조성.txt")
T = int(input())
dy = [0,1,1,-1]
dx = [-1,0,1,0]

for test_case in range(1,T+1):
    N,k = map(int,input().split())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    visited = [[False]*N for _ in range(N)]
    # pprint(visited)
    mx = max(max(matrix))
    road_len = []
    max_len = 0
    
    for y in range(N):
        for x in range(N):        
            if not visited[y][x] and matrix[y][x] == mx :
                stack = [(y,x)]
                visited[y][x] = True
                length = 0
                # dfs
                for kv in range(k): # kv를 사용하면 k_flag를 True로 만든다.
                    k_flag = False
                    while stack != []:
                        dfs_y,dfs_x = stack.pop()
                        length += 1
                        # 이제 여기서 이동 좌표값이 0~k만큼 딱 한번 변화할 수 있는데..
                        # k를 사용하는 경우 == 이동좌표값이 원래 좌표와 같을때..
                        # 방문리스트도 받아와야하나..
                        for i in range(4):
                            ny = dfs_y + dy[i]
                            nx = dfs_x + dx[i]
                            if not (0 <= ny < N and 0 <= nx < N): # 범위
                                continue
                            if not (not k_flag and matrix[ny][nx] == matrix[dfs_y][dfs_x]):
                                k_flag == True
                                matrix[ny][nx] = matrix[ny][nx] - kv
                            if not (matrix[ny][nx] < matrix[dfs_y][dfs_x]) :
                                continue
                            if visited[ny][nx] == True:
                                continue
                            stack.append((ny,nx))
                            visited[ny][nx] = True
                    road_len.append(length)
                    # if max_len < length:
                    #     max_len = length
    result = road_len  
    print(f'#{test_case} {result}')