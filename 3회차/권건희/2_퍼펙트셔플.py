import sys

sys.stdin = open("_퍼펙트셔플.txt")

T=int(input())
for _ in range(T):
    N=int(input())
    li1=list(input().split())
    li2=[]
    if N%2==0:
        for r in range(N//2):
            li2.append(li1[r])
            li2.append(li1[r+(N//2)])
    if N%2!=0:
        for j in range((N//2)+1):
            if j!=(N//2):
                li2.append(li1[j])
                li2.append(li1[j+(N//2)+1])
            else:
                li2.append(li1[j])
    print(f'#{_+1} ',end='')
    print(*li2)

