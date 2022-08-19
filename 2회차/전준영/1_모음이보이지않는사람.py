import sys

sys.stdin = open("_모음이보이지않는사람.txt")
T=int(input())
dic=['a','e','i','o','u']
answer=[]
for _ in range(T):
    str0=input()
    for i in str0:
        if(i in dic):
            str0=str0.replace(i,'')
    answer.append(str0)
cnt=1
for m in answer:
    print("#"+str(cnt),m)
    cnt+=1
