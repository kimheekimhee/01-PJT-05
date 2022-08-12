import sys

sys.stdin = open("_반반.txt")

T = int(input())

for tc in range(T):
    a = input()
    a = list(a)
    if len(set(a)) == 2:
        print(f'#{tc+1} Yes')
    else:
        print(f'#{tc+1} No')