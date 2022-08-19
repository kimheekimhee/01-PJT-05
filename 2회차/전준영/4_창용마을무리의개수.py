import sys

sys.stdin = open("_창용마을무리의개수.txt")
T=int(input())
answer=[]
for _ in range(T):
    N,M=map(int,input().split())
    arr=[[] for _ in range(N+1)]
    group=[]
    for i in range(1,N+1):
        group.append(i)
    cnt=0
    for _ in range(M):
        a,b=map(int,input().split())
        arr[a].append(b)
        arr[b].append(a)
    stack=[]
    while group:
        temp=group.pop()
        cnt+=1
        stack.append(temp)
        while stack:
            temp=stack.pop()
            for i in arr[temp]:
                if(i in group):
                    group.remove(i)
                    stack.append(i)
    answer.append(cnt)
cnt=1
for m in answer:
    print("#"+str(cnt),m)
    cnt+=1