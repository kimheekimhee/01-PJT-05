import sys

sys.stdin = open("_Flatten.txt")

for i in range(1, 11):
    dump = int(input())

    box = list(map(int, input().split()))

    for _ in range(dump):
        max_idx = box.index(max(box))
        min_idx = box.index(min(box))

        box[max_idx] -= 1
        box[min_idx] += 1

    f_max = box.index(max(box))
    f_min = box.index(min(box))

    print(f'#{i} {box[f_max] - box[f_min]}')
