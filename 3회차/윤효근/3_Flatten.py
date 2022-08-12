import sys

sys.stdin = open("_Flatten.txt")
for test_case in range(1,11):
    limit = int(input())
    h = list(map(int,input().split()))
    h.sort()

    aver = sum(h)//len(h)
    while True:
        h[h.index(max(h))] -= 1
        h[h.index(min(h))] += 1
        limit -= 1
        if limit == 0:
            break

    print(f'#{test_case} {(max(h)-min(h))}')

