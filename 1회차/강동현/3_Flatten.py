import sys

sys.stdin = open("_Flatten.txt")

for z in range(1,11):
    dump = int(input())
    boxes = list(map(int, input().split()))
    for _ in range(dump+1):
        maxbox = max(boxes)
        minbox = min(boxes)
        boxes[boxes.index(maxbox)] -=1
        boxes[boxes.index(minbox)] +=1
    print(f'#{z} {maxbox - minbox}')