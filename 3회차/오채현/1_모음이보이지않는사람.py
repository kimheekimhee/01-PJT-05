import sys

sys.stdin = open("_모음이보이지않는사람.txt")


T = int(input())

for test_case in range(T):
    vowel = 'aeiou'
    word = input()
    for char in word:
        if char in vowel:
            word = word.replace(char, '')
    print(f'#{test_case} {word}')
