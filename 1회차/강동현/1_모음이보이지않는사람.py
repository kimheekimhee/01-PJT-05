import sys

sys.stdin = open("_모음이보이지않는사람.txt")

T = int(input())
for z in range(T):
    word = input()
    nwrd = ''
    for i in range(len(word)):
        if word[i] in 'aeiou':
            continue
        else:
            nwrd += word[i]
    print(f'#{z+1} {nwrd}')