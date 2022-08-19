import sys

sys.stdin = open("_퍼펙트셔플.txt")
tc=int(input())
for i in range(tc):
    n=int(input())
    s=list(map(str, input().split()))
    s1=[]
    result=[]
    if n%2 == 0 :
        for j in range(n//2,n):
            s1.append(s[j])
        for j in range(n//2):
            result.append(s[j])
            result.append(s1[j])
    else :
        for j in range((n//2)+1,n):
            s1.append(s[j])
        for j in range(n//2):
            result.append(s[j])
            result.append(s1[j])
        result.append(s[n//2])
    
    print(f'#{i+1}',*result)