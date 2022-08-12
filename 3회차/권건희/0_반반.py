import sys

sys.stdin = open("_반반.txt")

T=int(input())
for _ in range(T):
    S1=input()
    S2=set(S1)
    cnt=0
    for i in S2:
        if S1.count(i)==2:
            cnt+=1
    if cnt==2:
        print(f'#{_+1} Yes')
    else:
        print(f'#{_+1} No')            
