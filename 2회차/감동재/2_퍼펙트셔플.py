import sys

sys.stdin = open("_퍼펙트셔플.txt")

T = int(input())



testcase = 1

for testcase in range(1,T+1):

    length = int(input())

    half = length//2

    s = input().split()

    a =[]
    b =[]

    if length %2 == 1:
       a = s[0:half+1]
       b = s[half+1:length]
    else:
       a = s[0:half]
       b = s[half:length] 
    

    print(f"#{testcase}",end=" ")

    for i in range(0,half):
        print(a[i],b[i], end =" ")

    if length%2 == 1 :
        print(a[half])
    else:
        print()
