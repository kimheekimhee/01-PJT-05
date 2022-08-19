import sys

sys.stdin = open("_모음이보이지않는사람.txt")

T = int(input())

for tc in range(1, T + 1):
    word = input()
    moum = ['a', 'e', 'i', 'o', 'u']

    result = ''
    for ch in word:
        if ch not in moum:
            result += ch

    print(f'#{tc}', result)

