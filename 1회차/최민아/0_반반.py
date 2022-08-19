import sys

sys.stdin = open("_반반.txt")

TC = int(input())                       # 테스트케이스 개수

for test_case in range(1, TC+1):
    S = input().strip()                 # 길이 4의 영대문자 문자열
    answer = 'No'                       # 대답 초기값 No

    for c in S:                         # 모든 알파벳 순서대로 확인
        if S.count(c) == 2:             # 해당 알파벳이 2번 등장하면
            S = S.replace(c, '')        # 해당 문자열 제거
     
    if S == '':                         # 문자열이 비어있으면
        answer = 'Yes'                  # 2개 문자가 2번씩 조건 만족 Yes
        
    print(f'#{test_case} {answer}')     # 대답 출력