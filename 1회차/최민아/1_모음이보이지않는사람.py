import sys

sys.stdin = open("_모음이보이지않는사람.txt")

T = int(input())                    # 테스트케이스 개수
no_read = 'aeiou'                   # 모음이 보이지 않음

for test_case in range(1, T+1):
    S = input().strip()             # 영소문자 단어

    for c in S:                     # 모든 알파벳 순서대로 확인
        if c in no_read:            # 알파벳이 모음이면
            S = S.replace(c, '')    # 해당 알파벳 제거

    print(f'#{test_case} {S}')      # 모음을 제외한 단어 출력