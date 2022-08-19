import sys

sys.stdin = open("_반반.txt")

t = int(input())
for _ in range(1,t+1):
    s = input()
    cnt = 'Yes'
    for i in range(4):
        if s.count(s[i]) == 2:
            pass
            
            
        else:
            cnt = 'No'
    if cnt == 'Yes':
        print(f'#{_} {cnt}')
    else: 
        print(f'#{_} {cnt}')
