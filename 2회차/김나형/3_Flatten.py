import sys

sys.stdin = open("_Flatten.txt")

T = 10
for tc in range(1, T + 1):
    dump = int(input())
    box = list(map(int, input().split()))
    for j in range(dump):
        m = max(box)
        n = min(box)
        box.remove(m)
        box.remove(n)
        max_num = m - 1
        min_num = n + 1
        box.append(max_num)
        box.append(min_num)
    print(f'#{tc} {max(box) - min(box)}')


