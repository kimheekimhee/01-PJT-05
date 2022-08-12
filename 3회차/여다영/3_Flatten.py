import sys

sys.stdin = open("_Flatten.txt")

for _ in range(1, 11):
    times = int(input())
    heights = list(map(int, input().split()))

    for i in range(times):
        max_height = max(heights)
        min_height = min(heights)

        for i in range(len(heights)):
            if heights[i] == max_height:
                heights[i] -= 1
                break
        for i in range(len(heights)):
            if heights[i] == min_height:
                heights[i] += 1
                break
            
    max_height = max(heights)
    min_height = min(heights)
    
    print(f'#{_}', max_height - min_height)