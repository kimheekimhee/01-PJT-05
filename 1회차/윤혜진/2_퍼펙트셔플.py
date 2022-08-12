# D3-퍼펙트 셔플



# 입력
'''
1. 테스트 케이스 수 T
2. 자연수 N
- 1 <= N <= 1,000
3. 덱에 카드가 놓인 순서대로 N개의 카드 이름이 공백으로 구분되어 주어짐
- 알파벳 대문자와 -으로만 이루어짐
- 0 < 길이 <= 80
'''



# 출력
'''
1. 주어진 덱을 퍼펙트 셔플한 결과를 한 줄에 카드 이름을 공백으로 구분하여 출력
<퍼펙트 셔플>
- 카드 덱을 정확히 반으로 나누고, 나눈 것들에서 교대로 카드를 뽑아 새로운 덱을 만드는 것
- 만약 N이 홀수이면, 교대로 놓을 때 먼저 놓는 쪽에 한 장이 더 들어가게 하면 됨
'''



# 코드 1
import sys
from collections import deque

sys.stdin = open("input_text/_퍼펙트셔플.txt")

T = int(input())

for test_case in range(1, T + 1):
    cnt = int(input())
    cards = input().split()

    # 카드 덱을 절반으로 나누기
    if cnt % 2 == 0:
        front = deque(cards[:cnt // 2])
        back = deque(cards[cnt // 2:])
    else:
        front = deque(cards[:cnt // 2 + 1])
        back = deque(cards[cnt // 2 + 1:])
    
    # 교대로 한 장씩 뽑아 쌓기
    rst = []
    while front or back:
        rst.append(front.popleft())
        if back:
            rst.append(back.popleft())
    
    print(f'#{test_case}', *rst)



# 실행시간(메모리:64,220 kb, 시간:185 ms)



# 코드 2
import sys
from collections import deque

sys.stdin = open("input_text/_퍼펙트셔플.txt")

T = int(input())

for test_case in range(1, T + 1):
    cnt = int(input())
    cards = input().split()

    # 카드 덱을 절반으로 나눠서 교대로 한 장씩 뽑아 쌓기
    front = 0   # 앞쪽 절반 카드 시작 인덱스
    back = end = cnt // 2 if cnt % 2 == 0 else cnt // 2 + 1   # 뒤쪽 절반 카드 시작 인덱스
    rst = []
    while front < end:
        rst.append(cards[front])
        if back < cnt:
            rst.append(cards[back])
        
        front += 1
        back += 1
    
    print(f'#{test_case}', *rst)



# 실행시간(메모리:61,692 kb, 시간:158 ms)