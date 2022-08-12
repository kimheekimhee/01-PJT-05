import sys

sys.stdin = open("_모음이보이지않는사람.txt")

T = int(input())
for tc in range(1, T+1):

    word = list(input())
    aeiou = ['a', 'e', 'i', 'o', 'u']
    arr = []

    for j in word:
        if j not in ['a', 'e', 'i', 'o', 'u']:
            arr.append(j)
            
    print(f'#{tc}', end=' ') 
    print(*arr, sep=(''))