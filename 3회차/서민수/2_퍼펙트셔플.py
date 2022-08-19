import sys

sys.stdin = open("_퍼펙트셔플.txt")

t= int(input())
for _ in (1,t+1):
    n,m = map(int,input().split())
    