import sys

sys.stdin = open("_모음이보이지않는사람.txt")

T=int(input())
for _ in range(T):
    S=input()
    for i in S:
        if i in 'aiueo':
            S=S.replace(i,'')
    print(f'#{_+1} {S}')
