import sys

sys.stdin = open("_반반.txt")

t = int(input())

for tc in range(t):
    word = sorted(list(input()))
    if word[0] == word[1] and word[2] == word[3] and word[1] != word[2]:
        print(f'#{tc+1} Yes')
    else:
        print(f'#{tc+1} No')