from pprint import pprint
import sys

sys.stdin = open("_모음이보이지않는사람.txt")

# congratulation 라는 단어를 보게 되면
# 모음을 뺀 cngrtltn 으로 인식

# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다
# 각 테스트 케이스의 첫 번째 줄에는
# 알파벳 소문자만으로 이루어진 단어가 주어진다
# 이 단어에 모음이 아닌 자음이 적어도 하나는 들어있다.

# 출력 예시
#1 cngrtltn
#2 synthtc
#3 fld

T = int(input())

vowel = 'aeiou'

for k in range(1, T + 1):
    word = list(input())
    # print(word)

    for i in vowel:
        for j in range(len(word)):
            if i == word[j]:
                word[j] = ''
    
    result = ''
    for i in word:
        result += i
    print('#{} {}'.format(k, result))