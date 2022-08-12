import sys
sys.stdin = open("_창용마을무리의개수.txt")
T=int(input())
for _ in range(T):
    N,M=map(int,input().split())
    people=[[]for _ in range(N+1)]
    for _ in range(M):
        i,j=map(int,input().split())
        people[i].append(j)
        people[j].append(i)
# 겹치는게 있으면 더하고 해당 리스트 삭제               
        




