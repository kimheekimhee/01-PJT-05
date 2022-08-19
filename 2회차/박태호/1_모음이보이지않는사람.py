import sys

sys.stdin = open("_모음이보이지않는사람.txt")
#알파벳에서 모음은 ‘a’, ‘e’, ‘i’, ‘o’, ‘u’의 다섯가지로 
# 예를 들어 “congratulation”이라는 단어를 당신이 보게 되면
#  “cngrtltn”으로 인식하게 될 것이다.
# 입력 
# 3
# congratulation
# synthetic
# fluid
aeiou = 'aeiou'
for _ in range(1,1+int(input())):
    word = input()
    ans = ''
    for w in word:
        if w not in aeiou:
            ans += w
    print(f'#{_} {ans}')