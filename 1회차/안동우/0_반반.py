from calendar import c
import sys


sys.stdin = open("_반반.txt")

TC= int(input())
for z in range(1,TC+1):
    s=list(input())

    a=0
    for q in s:
        if s.count(q) == 2:
            pass
        else:
            a=1
            break
    if  a == 1:
        print(f'#{z}','No')
 
    else:
        print(f'#{z}','Yes')
