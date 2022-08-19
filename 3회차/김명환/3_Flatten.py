import sys

sys.stdin = open("_Flatten.txt")
T = 10 
for i in range(T):
    N = int(input())
    li = list(map(int,input().split()))
    for j in range(N):
        max_of_li = max(li)
        min_of_li = min(li)
        idx_max = li.index(max_of_li)
        idx_min = li.index(min_of_li)
        li[idx_max] -= 1
        li[idx_min] += 1
    print(f'#{i+1} {max(li)-min(li)}')