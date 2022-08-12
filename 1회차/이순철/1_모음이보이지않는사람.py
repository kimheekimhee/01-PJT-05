import sys

sys.stdin = open("_모음이보이지않는사람.txt")

t = int(input())
for t_case in range(1, t + 1):

    word = input()
    for i in word:
        if i in 'aeiou':
            word = word.replace(i, '')
    print(f'#{t_case} {word}')