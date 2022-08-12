import sys

sys.stdin = open("_모음이보이지않는사람.txt")

test_case = int(input())
for test in range(1, test_case + 1):
    word = input()
    check = 'aeiou'
    result = ''
    for i in word:
        if i not in check:
            result += i
    print(f'#{test} {result}')
    # 주어진 문자열을 순회하며 모음 aeiou를 제외한 문자들을 포함한 새로운 문자열을 만들어 출력합니다.