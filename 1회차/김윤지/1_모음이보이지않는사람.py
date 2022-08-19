import sys

sys.stdin = open("_모음이보이지않는사람.txt")

t = int(input())

for tc in range(1,t+1):
    word = input()
    new = ''

    for i in word:
        if i != 'a' and i != 'e' and i != 'i' and i != 'o' and i != 'u':
            new += i
    print(f'#{tc} {new}')

#새로운문자열 new에 i가 모음이 아니면 하나씩 더하기.