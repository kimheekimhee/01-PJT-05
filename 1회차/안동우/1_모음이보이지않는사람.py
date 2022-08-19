from re import T
import sys


sys.stdin = open("_모음이보이지않는사람.txt")

T=int(input())
TC=['a','e','i','o','u']
a=[]
b=set(['c'])
for z in range(1,T+1):
    a.append(list(input()))
print(a-b)
