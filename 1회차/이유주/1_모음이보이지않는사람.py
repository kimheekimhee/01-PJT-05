import sys

sys.stdin = open("_모음이보이지않는사람.txt")


vowel = ['a', 'e', 'o', 'u', 'i']
T = int(input())
for i in range(1, T+1):
    word = input()
    for x in word:
        if x in vowel:
            word = word.replace(x, '')
    print(f'#{i} {word}')    

