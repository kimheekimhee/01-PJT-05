import sys

sys.stdin = open("_Flatten.txt")
for i in range(10):
    dump = int(input())
    box_arr = sorted(list(map(int, input().split())))
    
    while dump:
        for j in range(len(box_arr)):
            if box_arr[j] == min(box_arr):
                box_arr[j] += 1
                break
        for k in range(len(box_arr)):
            if box_arr[k] == max(box_arr):
                box_arr[k] -= 1
                break
        dump -= 1
    print(f'#{i + 1}',max(box_arr) - min(box_arr))
        
            
