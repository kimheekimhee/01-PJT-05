import sys

sys.stdin = open("_모음이보이지않는사람.txt")

T = int(input())
collection = ['a', 'e', 'i', 'o', 'u']

for tc in range(1, T + 1):
    S = list(input())
    for j in collection:
        while j in S:
            S.remove(j)
        
    print(f'#{tc} {"".join(S)}')
