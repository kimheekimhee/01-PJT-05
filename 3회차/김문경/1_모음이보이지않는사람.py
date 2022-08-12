import sys

sys.stdin = open("_모음이보이지않는사람.txt")

T = int(input())
moeum = ['a', 'e', 'i', 'o', 'u']

for test_case in range(1 ,T + 1):
    word = input()
    result = ''
    for char in word:
        if char not in moeum:
            result += char
    print(f'#{test_case} {result}')   