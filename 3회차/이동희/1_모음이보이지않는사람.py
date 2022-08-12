import sys

sys.stdin = open("_모음이보이지않는사람.txt")

n = int(input())
for tc in range(1,n+1):
    word = input()

    for i in word:
        if i in ['a','e','i','o','u']:
            word = word.replace(i,'')
    print(f'#{tc} {word}')