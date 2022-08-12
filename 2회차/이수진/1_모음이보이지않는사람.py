import sys

from numpy import intp

sys.stdin = open("_모음이보이지않는사람.txt")

tc=int(input())
for i in range(tc):
    s=input().replace('a','').replace('e','').replace('i','').replace('o','').replace('u','')
    print(f'#{i+1} {s}')
    