import sys

sys.stdin = open("_반반.txt")

t = int(input())

for i in range(1, t + 1):
    s = input()
    chk = set(s)

    len_ = len(s) - len(chk)

    if len_ == 2 and len(chk) == 2:
        print(f'#{i} Yes')
    else:
        print(f'#{i} No')
