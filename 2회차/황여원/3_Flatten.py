import sys

sys.stdin = open("_Flatten.txt")

T = 10 
for tc in range(1,T+1) : 
    # 덤프 횟수 
    dump = int(input())
    # 각 상자의 높이 값 
    box = list(map(int,input().split()))

    for i in range(dump) : 
        # 최댓값 최솟값 구해주고
        max_ = max(box)
        min_ = min(box)

        # 최대,최소 인덱스를 찾아서
        index_max = box.index(max_)
        index_min = box.index(min_)
        
        # 내려주고 올려주기 
        box[index_max] -= 1
        box[index_min] += 1

        # 최댓값과 최솟값 차이 
        result = max(box)-min(box)

    print(f'#{tc} {result}')