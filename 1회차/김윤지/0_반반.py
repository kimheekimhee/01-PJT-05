import sys

sys.stdin = open("_반반.txt")

t = int(input())

for tc in range(1,t+1):
    s = sorted(list(input()))

    if s[0]==s[1] and s[2]==s[3] and s[1] != s[2]:
        print(f'#{tc} {"Yes"}')
    else:
        print(f'#{tc} {"No"}')