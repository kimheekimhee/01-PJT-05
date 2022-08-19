import sys

sys.stdin = open("_Flatten.txt")
from collections import deque

for ts in range(1, 11):
    N = int(input())
    boxes = list(map(int, input().split()))

    for a in range(1,N+1):
        boxes = deque(sorted(boxes))
        boxes.append(boxes.pop()-1)
        boxes.append(boxes.popleft()+1)
    print(f'#{ts} {max(boxes)-min(boxes)}')