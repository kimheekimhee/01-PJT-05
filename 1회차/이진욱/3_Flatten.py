import sys

sys.stdin = open("_Flatten.txt")



for t in range(10):
    
    
    N = int(input())
    
    N_list = list(map(int,input().split()))
    
    
    for i in range(N):
        N_list.sort()
    
        max_N = N_list.pop()
    
        N_list.sort(reverse=True)
    
        min_N = N_list.pop()
    
        max_N -= 1
        min_N += 1
    
        N_list.append(max_N)
        N_list.append(min_N)
    
    print(f'#{t+1} {max(N_list)-min(N_list)}'        )
    
    
    
