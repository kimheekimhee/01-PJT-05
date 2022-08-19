import sys

sys.stdin = open("_Flatten.txt")
answer=[]
def switch(array,i,k):
    temp=array[i]
    array[i]=k
    array[k]=temp
    return 1
for _ in range(10):
    num=int(input())
    arr=list(map(int,input().split()))
    length=100
    arr.sort()
    b0=0
    for _ in range(num):
        arr[0]+=1
        arr[length-1]-=1
        arr.sort()
    sub=arr[length-1]-arr[0]
    answer.append(sub)
cnt=1
for m in answer:
    print("#"+str(cnt),m)
    cnt+=1