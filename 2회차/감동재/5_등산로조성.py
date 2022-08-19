import sys

sys.stdin = open("_등산로조성.txt")

from collections import deque

T = int(input())


dj = [-1,0,1,0]
di = [0,1,0,-1]

for _ in range(1,T):

    N , K = list(map(int,input().split()))

    _point = deque([])
    
    print(N , K)

    _map =[]

    _index = []


    _max = 0

    for i in range(N):
        s = list(map(int,input().split()))
        _max = max(_max,max(s))
        _map.append(s)

 
    for i in range(N):
        for j in range(N):
            if _max == _map[i][j]:
                _point.append((i,j))

    
    
    while len(_point) != 0:

        tmp_point = _point.pop() 

        stack = deque([tmp_point])

        visited = [[0 for _ in range(0,N)] for _ in range(0,N)]

        count = [[0 for _ in range(0,N)] for _ in range(0,N)]
    
        while len(stack) != 0:

           _pop = stack.pop()
           
           i = _pop[0]
           j = _pop[1]
           start_h = s[i][j]
           

           for k in range(4):
                I = i+di[k]
                J = j+dj[K]

                if 0<= I < N and 0<= J < N and visited[I][J] ==1 and s[i][j] > s[I][J]:
                    count[I][J] = count[i][j]+1





            




            


