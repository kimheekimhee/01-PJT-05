import sys

sys.stdin = open("_퍼펙트셔플.txt")

N = int(input())

for i in range (1,N+1):
    result = []
    count = int(input()) 
    string = list(input().split())
    if count %2 == 0:
        a = int(count / 2 )
    else:
        a = int((count / 2 ) +1)
        
    for a_ in range(a):
        result.append(string.pop(0))
    index =1 
    while(1):
        result.insert(index,string.pop(0))
        index +=2
        if len(result) == count:
            break
    print(f'#{i} ',end=' ')
    for k in result:
        print(k,end=' ')
    print()
 
        
    
        
        
 