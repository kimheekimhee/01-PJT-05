import sys

sys.stdin = open("_Flatten.txt")

T = 10

for test_case in range(1, T+1):
    dmp = int(input())
    boxs = list(map(int, input().split()))
    n = len(boxs)

    total = int(sum(boxs) / n)

    while dmp:
        mx = max(boxs)
        mn = min(boxs)
        # if (mx - mn) == 1 or (mx - mn) == 0:
        #     print(mx - mn)
        #     break
        x = boxs.index(mx)
        y = boxs.index(mn)
        boxs[x] -= 1
        boxs[y] += 1
        dmp -= 1

    print(f'#{test_case}', max(boxs) - min(boxs))


# for i in range(n):
    #     mx = max(boxs)
    #     mn = min(boxs)
    # print(boxs)
    # mx = max(boxs)
    # mn = min(boxs)
    # x = boxs.index(mx)
    # y = boxs.index(mn)
    # boxs[x] -= 1
    # boxs[y] += 1
    # print(boxs)
