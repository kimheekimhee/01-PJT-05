import sys

sys.stdin = open("_모음이보이지않는사람.txt")

nosee = ['a','e','i','o','u']

for t in range(1, int(input())+1):
    word = input()
    for ns in nosee:
        word= word.replace(ns,'')
    print(f'#{t} {word}')