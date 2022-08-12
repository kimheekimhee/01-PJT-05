import sys

sys.stdin = open("_Flatten.txt")

T = 10 
for tc in range(1,T+1) : 
    # 덤프 횟수 
    dump = int(input())
    # 각 상자의 높이 값 
    box = list(map(int,input().split()))

    for i in range(dump) : 
        # 최댓값 최솟값 구해주고,,그 값이 어디있는지 찾아서...?
        max_ = max(box)
        min_ = min(box)
        
        