# SWEA 4406. 모음이 보이지 않는 사람

import sys

sys.stdin = open("_모음이보이지않는사람.txt")

T = int(input())
vowels = ['a', 'e', 'i', 'o', 'u']

for i in range(1, T+1):
    S = input()

    for j in vowels:
        if j in S:
            S = S.replace(j, '')

    print(f'#{i} {S}')