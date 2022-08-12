import sys

sys.stdin = open("./3회차/신윤식/_모음이보이지않는사람.txt")

lst = ['a', 'e', 'i', 'o', 'u']

T = int(input())

for _ in range(1, T+1):
    word = input()
    for i in lst:
        word = word.replace(i,'')
    
    print(f'#{_} {word}')
