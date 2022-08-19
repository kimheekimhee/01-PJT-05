import queue
import sys
import math
from collections import deque

sys.stdin = open("_퍼펙트셔플.txt")

T = int(input())
for t in range(1, T+1):
    print(f'#{t}', end=' ')
    n = int(input())
    list_ = list(input().split())
    # 앞 문자들 덱 생성
    front = deque()
    # 뒷 문자들 덱 생성
    back = deque()

    # n/2를 올림한 수만큼 문자들을
    for i in range(math.ceil(n / 2)):
        # front에 저장
        front.append(list_[i])
    # 나머지 숫자들
    for i in range(math.ceil(n / 2), n):
        # back에 저장
        back.append(list_[i])

    while True:
        # indexError 예외처리
        try:
            # front, back에 있던 요소들이 전부 빠지면
            if len(front) == 0 and len(back) == 0:
                # 한 줄 띄우기
                print()
                # 반복 중지
                break
            # front, back에 요소가 남아있으면
            else:
                # front 요소 먼저 뺀 후 back 요소 빼기
                print(front.popleft(), end=' ')
                print(back.popleft(), end=' ')
        # 에러나도 무시하고 이어가기
        except:
            continue