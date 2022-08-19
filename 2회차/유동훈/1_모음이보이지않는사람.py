# import sys

# sys.stdin = open("_모음이보이지않는사람.txt")

vowel = ['a', 'e', 'i', 'o', 'u']

T = int(input())
for i in range(1, T+1):
    word = input()
    for j in vowel:
        word = word.replace(j,'')

    print(f'#{i} {word}')