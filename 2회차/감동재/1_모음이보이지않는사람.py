import sys

V =['a','e','i','o','u']

sys.stdin = open("_모음이보이지않는사람.txt")

T = int(input()) 


for testcase in range(1,T+1):
    
    s = input()

    tmp = []
    i = 0

    for v in V:
        if i == 0 :
            tmp.append(s.replace(v,""))
        else:
            tmp.append(tmp[i-1].replace(v,""))
        
        i+=1

    print(f"#{testcase} {tmp[4]}")
