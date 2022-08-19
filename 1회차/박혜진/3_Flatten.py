import sys

sys.stdin = open("_Flatten.txt")

for num in range(1, 11) :
    n = int(input())
    box = list(map(int, input().split()))


    for _ in range(n) :
        max_in = box.index(max(box))
        box[max_in] = box[max_in] - 1

        min_in = box.index(min(box))
        box[min_in] = box[min_in] + 1

    print(f'#{num} {max(box)-min(box)}')