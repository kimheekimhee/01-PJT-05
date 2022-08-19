import sys

sys.stdin = open("_Flatten.txt")

t = 10
for case in range(1, t+1):
    dumping = int(input())
    numbering = list(map(int, input().split()))
    for i in range(dumping):
        max_height = numbering.index(max(numbering))
        min_height = numbering.index(min(numbering))
        numbering[max_height] -= 1
        numbering[min_height] += 1
    print(f'#{case} {max(numbering)-min(numbering)}')