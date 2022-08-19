import sys

sys.stdin = open("_Flatten.txt")

for tc in range(10):
    D = int(input())
    li = list(map(int,input().split()))
    for _ in range(D):
        li[li.index(max(li))] -= 1
        li[li.index(min(li))] += 1
    print(f'#{tc+1} {max(li)-min(li)}')