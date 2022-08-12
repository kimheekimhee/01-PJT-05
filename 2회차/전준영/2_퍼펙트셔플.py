import sys

sys.stdin = open("_퍼펙트셔플.txt")
T=int(input())
dic=['a','e','i','o','u']
answer=[]
for _ in range(T):
    length=int(input())
    arr=input().split()
    if(length%2==0):
        arr0=arr[:length//2]
        arr1=arr[length//2:]
        arr=[]
        for i in range(length):
            if(i%2==0):
                arr.append(arr0[i//2])
            else:
                arr.append(arr1[i//2])
    else:
        arr0=arr[:length//2+1]
        arr1=arr[length//2+1:]
        arr=[]
        for i in range(length):
            if(i%2==0):
                arr.append(arr0[i//2])
            else:
                arr.append(arr1[i//2])
    answer.append(arr)
cnt=1
for m in answer:
    print("#"+str(cnt),end=' ')
    for k in m:
       print(k,end=' ')
    print()
    cnt+=1