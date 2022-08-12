import sys

sys.stdin = open("_모음이보이지않는사람.txt")
#소문자로만 이뤄진 문자열이 주어지는데, 모음뺴고 출력하기.

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    set_vowel = {'a', 'e', 'i', 'o', 'u'}

    word = input()
    print(f'#{test_case}', end = ' ')
    for i in word:
        if i in set_vowel:
            continue
        else:
            print(i, end = '')
    
    print()

        