import sys

sys.stdin = open("_반반.txt")

T = int(input())

for i in range(1, T+1):
    word = set(list(input()))
    if len(word) == 2:
        print(f'#{i} Yes')
    else:
        print(f'#{i} No')

