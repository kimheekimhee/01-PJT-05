import sys

sys.stdin = open("_Flatten.txt")

for i in range(1,11):
    
    N = int(input())
    lst = list(map(int,input().split()))
   
    for n in range(N):
        max_ = max(lst)
        min_ = min(lst)
        t1 = 0
        t2 = 0
        for n in range(len(lst)):
            if lst[n] == max_ and t1 == 0:
                lst[n] = lst[n]-1
                t1 = 1
    
            if lst[n] == min_ and t2 == 0:
                lst[n] = lst[n]+1
                t2 = 1
        # if max_ - min_ <= 1:
        #     break
    print(f'#{i} {max_ - min_}')

 