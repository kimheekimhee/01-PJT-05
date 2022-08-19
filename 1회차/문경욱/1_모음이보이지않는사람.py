# import sys

# sys.stdin = open("_모음이보이지않는사람.txt")

# 모음 리스트를 생성 후 글자가 모음 리스트 안에 없으면 새로운 문자열에 추가, 있으면 넘어가는 방식으로 풀었습니다.

# 모음 리스트 생성
vowel = ['a', 'e', 'i', 'o', 'u']

# 테스트 케이스 입력 받음
T = int(input())
for test_case in range(1, T+1):
    # 단어 입력 받음
    word_ = input()
    
    # 출력할 새로운 문자열 선언
    no_vowel = ''

    # 입력 받은 단어에서 한 글자씩 뽑아서
    for elem in word_:
        # 그 단어가 vowel 리스트 안에 없으면, 즉 자음이면
        if elem not in vowel:
            # 새로운 문자열에 추가
            no_vowel += elem
        # 모음이면 continue
        else:
            continue

    print(f'#{test_case} {no_vowel}')