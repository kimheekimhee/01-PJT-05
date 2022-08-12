import sys

sys.stdin = open("_모음이보이지않는사람.txt")


T = int(input())

moum = ['a', 'e', 'i', 'o', 'u', 'y']

for t in range(1, T+1) :
    word = input()

    for i in moum :
        word = word.replace(i, '')

    print(f'#{t} {word}')

