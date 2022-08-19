import sys

sys.stdin = open("_모음이보이지않는사람.txt")

T = int(input()) # 테스트 케이스 T가 주어진다.
for i in range(1, T + 1):
    word = input()
    result = ''
 
    for j in range(len(word)):
        if word[j] in ['a', 'e', 'i', 'o', 'u']: # 모음['a', 'e', 'i', 'o', 'u'] 리스트 생성
            continue # continue 함수를 사용해서 코드 실행 건너뛴다.
        result += word[j] # 모음 이외에 다른 문자 출력
 
    print('#{} {}'.format(i, result))