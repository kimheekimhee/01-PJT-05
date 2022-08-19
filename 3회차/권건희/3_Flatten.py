import sys

sys.stdin = open("_Flatten.txt")
T=10
for _ in range(T):
    N=int(input())
    Box=list(map(int,input().split()))
    while N!=0:
        if max(Box)-min(Box)==0 or max(Box)-min(Box)==1 :
            break
        else:
            i=Box.index(max(Box))
            j=Box.index(min(Box))
            Box[i]=Box[i]-1
            Box[j]=Box[j]+1
            N=N-1
    print(f'#{_+1} {max(Box)-min(Box)}')    
