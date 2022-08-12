import sys

sys.stdin = open("_모음이보이지않는사람.txt")

T = int(input())

aeiou = ['a', 'e', 'i', 'o', 'u']

for i in range(1, T+1):
    S = input()
    for idx in aeiou:
        S = S.replace(idx, '')
    print(f'#{i} {S}')