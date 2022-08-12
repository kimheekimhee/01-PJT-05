import sys
import heapq

sys.stdin = open("./3회차/신윤식/_Flatten.txt")

for _ in range(1, 11):
    dump_num = int(input())
    lst = list(map(int,input().split()))

    for i in range(dump_num):
        heapq.heapify(lst)

        a = heapq.heappop(lst)
        a += 1
        heapq.heappush(lst,a)

        lst = sorted(lst)
        b = lst.pop()
        b = b-1
        lst.append(b)

        if a == b or a == b+1:
            break

    print(f'#{_} {max(lst)-heapq.heappop(lst)}')