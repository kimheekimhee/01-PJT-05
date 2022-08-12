

import sys

sys.stdin = open("_창용마을무리의개수.txt")

from collections import deque

T = int(input())

for testcase in range(1,T+1):

    N,M = list(map(int,input().split()))

    person = [[] for _ in range(N+1)]

    for _ in range(M):
        i , n = list(map(int,input().split()))
        person[i].append(n)
        person[n].append(i)
        
    check = [0 for _ in range(N+1)]

    s = deque([])

    s.append(1)
    check[1] = 1

    
    cnt = 1

    while True:

        while len(s)!=0 :

            _pop = s.pop()


            for a in person[_pop]:
                if check[a] == 0:
                    s.append(a)
                    check[a] = 1

        
        if sum(check) == N:
            print(f"#{testcase} {cnt}")
            break
        else:
            for i in range(1,len(check)):
                if check[i] == 0:
                    s.append(i)
                    cnt+=1
                    check[i] = 1
                    break
          