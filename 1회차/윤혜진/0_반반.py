# D3-반반



# 입력
'''
1. 테스트 케이스 수
2. 길이 4의 알파벳 대문자로 이루어진 문자열 S
'''



# 출력
'''
1. 문자열 S에 정확히 두 알파벳이 2개 등장하고 각각 두 번 등장하면 Yes 출력, 아니면 No 출력
'''



# 코드 1
import sys

sys.stdin = open("input_text/_반반.txt")

T = int(input())

for test_case in range(1, T + 1):
    S = input()
    answer = 'Yes'
    
    # ord('A') = 65, ord('Z') = 90
    alph = [0] * 26

    for char in S:
        num = ord(char) - 65
        alph[num] += 1

    for cnt in alph:
        if cnt != 0 and cnt != 2:
            answer = 'No'
    
    print(f'#{test_case} {answer}')
    


# 실행결과(메모리:56,692 kb, 시간:131 ms)



# 코드 2
import sys

sys.stdin = open("input_text/_반반.txt")

T = int(input())

for test_case in range(1, T + 1):
    S = sorted(input())
    answer = 'Yes'

    if S[0] != S[1] or S[2] != S[3] or S[0] == S[2]:
        answer = 'No'
    
    print(f'#{test_case} {answer}')



# 실행결과(메모리:56,936 kb, 시간:127 ms)



# 코드 3
import sys

sys.stdin = open("input_text/_반반.txt")

T = int(input())

for test_case in range(1, T + 1):
    S = sorted(input()) 
    answer = 'No'

    if S.count(S[0]) == 2 and S.count(S[2]) == 2:
        answer = 'Yes'
    
    print(f'#{test_case} {answer}')
    


# 실행결과(메모리:56,688 kb, 시간:134 ms)



# 코드 4
import sys
from collections import Counter

sys.stdin = open("input_text/_반반.txt")

T = int(input())

for test_case in range(1, T + 1):
    S = Counter(input())
    answer = 'Yes'

    if len(S) != 2:
        answer = 'No'

    for cnt in S.values():
        if cnt != 2:
            answer = 'No'

    print(f'#{test_case} {answer}')



# 실행결과(메모리:60,360 kb, 시간:167 ms)