import sys

sys.stdin = open("_Flatten.txt")

for t in range(1,11):
    n = int(input())
    heights = list(map(int,input().split()))
    for i in range(n):
        mx_height = max(heights)
        min_height = min(heights)
        mx_h_index = heights.index(mx_height)
        min_h_index = heights.index(min_height)
        heights[mx_h_index]-=1
        heights[min_h_index]+=1
    gap = max(heights)-min(heights)
    print(f'#{t}',gap)