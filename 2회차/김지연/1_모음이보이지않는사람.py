import sys

sys.stdin = open("_모음이보이지않는사람.txt")

T = int(input())

for tc in range(1, T+1): 
    s = input()
    result = ''

    for char in s:
        if char != 'a' and char != 'e' and char != 'i' and char != 'o' and char != 'u':
            result += char
    print('#{} {}'.format(tc, result))