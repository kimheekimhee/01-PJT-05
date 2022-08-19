import sys

sys.stdin = open("_모음이보이지않는사람.txt")

T = int(input())

for ts in range(1, T+1):
    alp= ['a', 'e', 'i', 'o', 'u',]
    N = input()
    for a in alp:
        N = N.replace(a,'')
    print(f'#{ts} {N}')