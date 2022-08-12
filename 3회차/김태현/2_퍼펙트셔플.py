from collections import deque
import sys
sys.stdin = open("_퍼펙트셔플.txt")

# 절반을 슬라이싱해서 큐 2개 생성
# 각 큐에서 번갈아가며 결과 리스트에 추가

T = int(input())

for t in range(1, T+1):
    result = []

    length = int(input())
    card_list = input().split()

    first = deque()
    second = deque()

    for i in range(length):
        if i < (length / 2):
            first.append(card_list[i]) # deque(['A', 'B', 'C'])
        else:
            second.append(card_list[i]) # deque(['D', 'E', 'F'])
    
    for j in range(length):
        if j % 2 == 0:
            result.append(first.popleft())
        else:
            result.append(second.popleft())
    
    print(f"#{t}", *result)