import sys

sys.stdin = open("_모음이보이지않는사람.txt")
T = int(input())
moum = ['a', 'e', 'i', 'o', 'u']
for _ in range(1, T + 1):
    word = list(input())
    words = []
    result = ''
    for a in word:
        if a not in moum:
            words.append(a)
    for b in words:
        result += b
    print(f'#{_} {result}')