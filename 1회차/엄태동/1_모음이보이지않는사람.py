import sys

sys.stdin = open("_모음이보이지않는사람.txt")
T=int(input())
for i in range(T):
    word=input()
    word=word.replace('a','')
    word=word.replace('e','')
    word=word.replace('i','')
    word=word.replace('o','')
    word=word.replace('u','')
    print(f'#{i+1} {word}')