import sys

sys.stdin = open("_Flatten.txt")


def dump(x):
    mx = max(x)
    mn = min(x)
    x[x.index(mx)] = (mx - 1)
    x[x.index(mn)] = (mn + 1)
    return x

for t in range(1, 11):
    fx_num= int(input())
    box = list(map(int, input().split()))
    for _ in range(fx_num):
        dump(box)
    print(f'#{t} {max(box) - min(box)}')