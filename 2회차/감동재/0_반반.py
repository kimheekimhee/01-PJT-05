import sys

sys.stdin = open("_반반.txt")

testcase = 1


n = int(input())

for testcase in range(1,n+1):

    a = input()

    length = len(a)
    half = len(a)//2
    check = False

    s = [a[i] for i in range(0,len(a))]

    A = set(s)

    check = True

    for a in A:
        if s.count(a) != half:
            check = False
    
    if check:
        print(f"#{testcase} Yes")
    else :
        print(f"#{testcase} No")

  
    