import sys

sys.stdin = open("_모음이보이지않는사람.txt")

for num in range(1, int(input())+1) :
    word = input()

    for i in word :
        if i in 'aeiou' :
            word = word.replace(i, '')

    print(f'#{num} {word}')