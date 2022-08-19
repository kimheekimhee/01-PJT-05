import sys

sys.stdin = open("_모음이보이지않는사람.txt")

T = int(input())
for t in range(1, T +1):
    word = list(input())

    for idx in range(len(word)):
        char = word[idx]
        if char in 'aeiou':
            word[idx] = 0

    answer = ''
    for char in word:
        if char != 0:
            answer += char

    print(f'#{t} {answer}')