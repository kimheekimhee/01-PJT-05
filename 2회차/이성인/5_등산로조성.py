from pprint import pprint
import sys

sys.stdin = open("_등산로조성.txt")

N, K = map(int, input().split())
trail = []
viseted = [[False]*N for _ in range(N)]
for _ in range(N):
    data = list(map(int, input().split()))
    trail.append(data)
pprint(trail)
sx = [0,0,-1,1,90]
sy = [1,-1,0,0,90]
stack = []
check = 0
cnt_list = [0]
for y in range(1,2):
    for x in range(2,3):
        viseted_same = viseted
        for i in range(100):
            
            y_same = y
            x_same = x
            cnt = 1
            while True:
                check += 1
                for f in range(5):
                    ny = y_same + sy[f]
                    nx = x_same + sx[f]
                    if 0 <= ny and ny < N and 0 <= nx and nx < N:  
                        before = trail[y_same][x_same]
                        if before < trail[ny][nx]:
                            if viseted_same[ny][nx] == False:
                                print(trail[ny][nx])
                                y_same = ny
                                x_same = nx
                                cnt += 1
                                check = 0
                                break
                else:
                    if check >= 2:
                        break
                    cnt_list.append(cnt)
                    viseted_same[y_same][x_same] = True
                    cnt = 1
            pprint(viseted_same)
print((cnt_list))       
                
