from re import M
import sys

sys.stdin = open("_반반.txt")
TC=int(input())
answer=[]
for i in range(TC):
    t=input()
    temp={}
    bo=0
    for k in t:
        if(k not in temp):
            temp[k]=1
        else:
            temp[k]+=1
            if(temp[k]==2):
                bo+=1
    if(bo==2):
        answer.append("Yes")
    else:
        answer.append("No")
cnt=1
for m in answer:
    print("#"+str(cnt),m)
    cnt+=1
