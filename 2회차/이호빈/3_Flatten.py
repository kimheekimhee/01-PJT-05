import sys
from tkinter.tix import ButtonBox

sys.stdin = open("_Flatten.txt")
#테스트 케이스
T = 10
for tc in range(1, T +1):
    # 입력값을 받아주고
    dump = int(input())
    # 입력값을 int로 형변환을 해주고 list에 감싸준다.
    box = list(map(int, input().split()))
    #입력값의 범위만큼 돌아주면서
    for i in range(dump):
        #최댓값을 찾아준다.
        max_ = max(box)
        #최솟값을 찾아준다
        min_ = min(box)
        #최댓값의 인덱스를 찾아준다.
        max_index = box.index(max_)
        #최솟값의 인덱스를 찾아준다.
        min_index = box.index(min_)
        # 덤프 횟수만큼 최댓값은 계속 -1 빼주고 최솟값은 계속 +1 더해준다. 
        box[max_index] -= 1
        box[min_index] += 1
    #최종값은 문제에서 요구하는 것처럼 최고점 - 최저점이다.
    print(f"#{tc} {max(box) - min(box)}")
    