import sys

sys.stdin = open("_Flatten.txt")

for i in range(1, 11):
    dump = int(input())
    box = sorted(map(int, input().split()))

    for _ in range(dump):
        max_ = box.pop(99) - 1
        box.append(max_)
        min_ = box.pop(0) + 1
        box.append(min_)

        box = sorted(box)

        if max(box) - min(box) <= 1:
            break

    print(f'#{i} {max(box)-min(box)}')