import sys

sys.stdin = open("_Flatten.txt")
for i in range(10):
    dump_num=int(input())
    box_height=list(map(int, input().split()))
    for _ in range(dump_num):
        index_max=box_height.index(max(box_height))
        index_min=box_height.index(min(box_height))
        box_height[index_max]-=1
        box_height[index_min]+=1
        if max(box_height) - min(box_height)<=1:
            print(f'#{i+1} {max(box_height) - min(box_height)}')
            break
    print(f'#{i+1} {max(box_height) - min(box_height)}')