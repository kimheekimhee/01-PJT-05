import sys

sys.stdin = open("_모음이보이지않는사람.txt")

t = int(input())
moem ='aeiou'
for i in range(1,t+1):
    word = input()
    for chrc in word:
        if chrc in moem:
            word = word.replace(chrc,'')
    print(f'#{i} {word}')
