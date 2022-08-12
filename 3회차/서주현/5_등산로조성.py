import sys

sys.stdin = open("_등산로조성.txt")


import copy

T = int(input())

for t in range(1, T+1) :
    n, k = map(int, input().split())

    mt = []
    top_mt = 0
    for i in range(n) :
        mt.append(list(map(int, input().split())))
        if top_mt < max(mt[i]) :
            top_mt = max(mt[i])
    dxy = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]
    # print(top_mt)
    

    def dfs_mt(node1, node2) :
        
        
        
        result = 1
        for clap in range(1, top_mt+1) :
            # print('clap :', clap)
            stack = [[node1, node2, 1]]
            mt2 = copy.deepcopy(mt)   
            visited = [[0]* n for i in range(n)] 
            
            while stack :
                # print('while문 안')
                y, x, cnt = stack.pop()

                if visited[y][x] < cnt :
                    # print(y, x)
                    visited[y][x] = cnt
                    for i in range(4) :
                        ny = y + dxy[i][0]
                        nx = x + dxy[i][1]

                        if 0<= ny <= n-1 and 0<= nx <= n-1 :    
                            if 0 < visited[ny][nx] <= cnt : 
                                pass
                            else :
                                if cnt == clap and mt2[ny][nx] >= k : 
                                    mt2[ny][nx] -= k
                                if mt2[ny][nx] < mt2[y][x] :
                                    # print(ny, nx, clap, cnt, mt2[ny][nx], mt2[y][x])
                                    stack.append([ny, nx, cnt+1])
                                    # print(stack)
                                    if result < cnt+1 :
                                        result = cnt+1
                                    if ny == 4 and nx == 1 :
                                        print('여기야-----------------------------------------------------------------')

                                    if clap == 4 :
                                        print(stack)
            if result < clap :
                # print('return 시점 clap과 result', clap, result)
                return result

        return result
    
                             
    answer = 0
    for i in range(n) :
        for j in range(n) :
            if mt[i][j] == top_mt :
                # print('hi 여기는', i, j)
                result = dfs_mt(i, j)
                if answer < result :
                    answer = result

    print(f'#{t} {answer}')



#1 6
#2 3
#3 7
#4 4
#5 2
#6 12
#7 6
#8 7
#9 10
#10 19