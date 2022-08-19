# D3-모음이 보이지 않는 사람



# 입력
'''
1. 테스트 케이스 수 T
2. 알파벳 소문자 단어
- 0 < 길이 <= 50
'''



# 출력
'''
1. #{테스트 케이스} {모음이 제거된 단어}
'''



# 코드
import sys

sys.stdin = open("input_text/_모음이보이지않는사람.txt")

T = int(input())
alphs = {'a', 'e', 'i', 'o', 'u'}

for test_case in range(1, T + 1):
    word = input()
    
    rst = ''
    for char in word:
        if char not in alphs:
            rst += char

    print(f'#{test_case} {rst}')



# 실행결과(메모리:56,684 kb, 시간:128 ms)