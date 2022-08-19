import sys

sys.stdin = open("_반반.txt")

tc = int(input())
s = []

for i in range(1, tc + 1):
    s.append(list(input()))
    c = sorted(s)

    if c[0] == c[1] and c[2] == c[3]:
        print(f'#{i} Yes')
    else:    
        print(f'#{i} No')
