import sys
from copy import deepcopy
sys.stdin = open("_등산로조성.txt")
class coordinate:
    def __init__(self,ls,n,K):
        self.way=[[ls[0],ls[1]]]
        self.arr=[n]
        self.bo=1
        self.cnt=1
        self.K=K
    def append_way(self,ls,n,inp):
        if(inp==1):
            self.way.append([ls[0],ls[1]])
            self.arr.append(n)
            self.cnt+=1
        elif(inp==0):
            self.bo=0
            self.way.append([ls[0],ls[1]])
            self.arr.append(self.arr[self.cnt-1]-1)
            self.cnt+=1
vector=[[0,1],[1,0],[-1,0],[0,-1]]
answer=[]
T=int(input())
for _ in range(T):
    N,K=map(int,input().split())
    arr=[list(map(int,input().split())) for _ in range(N)]
    maxnode=[]
    max=0
    for i in range(N):
        for k in range(N):
            if(max<arr[i][k]):
                maxnode.clear()
                max=arr[i][k]
                maxnode.append([i,k])
            elif(max==arr[i][k]):
                maxnode.append([i,k])
    maxway=0
    for j in maxnode:
        node=coordinate(j,arr[j[0]][j[1]],K)
        stack=[]
        stack.append(node)
        ls=[0,0]
        while stack:
            temp=stack.pop()
            c=0
            for i in vector:
                ls[0]=temp.way[temp.cnt-1][0]+i[0]
                ls[1]=temp.way[temp.cnt-1][1]+i[1]
                if(0<=ls[0]<N and 0<=ls[1]<N):
                    n=arr[ls[0]][ls[1]]
                    if(n<temp.arr[temp.cnt-1] and ls not in temp.way):
                        ntemp=deepcopy(temp)
                        ntemp.append_way(ls,n,1)
                        stack.append(ntemp)
                        if(ntemp.cnt>maxway):
                            maxway=ntemp.cnt
                    elif(n-K<temp.arr[temp.cnt-1] and temp.bo==1 and ls not in temp.way):
                        ntemp=deepcopy(temp)
                        ntemp.append_way(ls,n,0)
                        stack.append(ntemp)
                        if(ntemp.cnt>maxway):
                            maxway=ntemp.cnt
    answer.append(maxway)
cnt=1
for m in answer:
    print("#"+str(cnt),m)
    cnt+=1