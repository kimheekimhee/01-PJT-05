import sys

sys.stdin = open("_모음이보이지않는사람.txt")

T = int(input())
mo = 'aeiou'

for t in range(T):
    word = input()
    new = ''
    for w in word:
        if w not in mo:
            new += w
    print(f'#{t+1} {new}')