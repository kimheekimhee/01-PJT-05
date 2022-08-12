import sys

sys.stdin = open("_반반.txt")

tc=int(input())

for i in range(tc):
    s=list(input())
    s.sort()
    print(f'#{i+1}',end=' ')
    if s[0] == s[1] and s[2] == s[3] and s[1] != s[2]:
        print('Yes')
    else :
        print('No')