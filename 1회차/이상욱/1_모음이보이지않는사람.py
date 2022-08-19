import sys

sys.stdin = open("_모음이보이지않는사람.txt")

word_list = ['a', 'e', 'i', 'o', 'u']
T = int(input())

for i in range(1, T+1):
    word = input()

    for j in range(len(word)):
        if word[j] in word_list:
           word = word.replace(word[j], ' ')
    word =word.replace(' ', '')
    print(f'#{i} {word}')

