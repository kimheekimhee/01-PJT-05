import sys

sys.stdin = open("_등산로조성.txt")

for test_case in range(1, int(input()) + 1):
    # 델타 4방향 ; 위 오른 아래 왼
    directions = [(-1, 0), (0, 1), (-1, 0), (0, -1)]

    # N, K, 전체 산 지형 입력받기
    N, K = map(int, input().split())
    field=[]
    for i in range(N):
        field.append(list(map(int, input().split())))

    # 출발점인 max값을 찾고 high 변수에 저장
    high = 0
    for line in field:
        now = max(line)
        if now > high:
            high = now

    # start_list에 값이 high인 x좌표, y좌표 쌍을 넣기
    start_list = []
    for x in range(N):
        for y in range(N):  
            if field[x][y] == high:
                start_list.append([x,y])
    
    # 출발점에서 한 번씩 돌리기
    for case in start_list:
        # 초기 설정
        cnt = 0
        cur_x = case[0]
        cur_y = case[1]
        delta_count = []
        for d in directions:
            new_y = cur_y + d[1]
            new_x = cur_x + d[0]
            # 범위 체크
            if not (-1 < new_y < N and -1 < new_x < N):
                continue
            # 이전보다 크거나 같으면 조건 불만족이므로 continue
            if field[new_x][new_y] >= field[cur_x][cur_y]:
                continue
            else:
                cur_x = new_x
                cur_y = new_y