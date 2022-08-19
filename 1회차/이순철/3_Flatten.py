import sys

sys.stdin = open("_Flatten.txt")

t = 10
for t_case in range(1, t + 1):
    dp = int(input())
    boxs = list(map(int, input().split()))
    # print(len(boxs), len(set(boxs)))

    while dp:
        boxs.append(boxs.pop(boxs.index(max(boxs))) - 1)
        boxs.append(boxs.pop(boxs.index(min(boxs))) + 1)
        dp -= 1

    print(f'#{t_case} {max(boxs) - min(boxs)}')
    