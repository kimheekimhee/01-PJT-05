import sys

sys.stdin = open("_Flatten.txt")

for t in range(1, 11):
    limit = int(input())
    boxes = list(map(int, input().split()))
    boxes = sorted(boxes)
    # print(boxes)

    for _ in range(limit):

        boxes[0] += 1
        boxes[len(boxes) -1] -= 1
        boxes = sorted(boxes)
        
    
    answer = boxes[len(boxes)  -1] - boxes[0]
    print(f'#{t} {answer}')