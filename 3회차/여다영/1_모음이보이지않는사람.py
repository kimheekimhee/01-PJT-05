import sys

sys.stdin = open("_모음이보이지않는사람.txt")

T = int(input())

vowels = ['a', 'e', 'i', 'o', 'u']

for _ in range(1, T + 1):
    string = input()

    for vowel in vowels:
        string = string.replace(vowel, '')

    print(f'#{_}', string)