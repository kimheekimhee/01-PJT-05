import sys

sys.stdin = open("_퍼펙트셔플.txt")

T = int(input())
for t in range(1, T+1):
    N = int(input())
    inputlst = list(input().split())
    if len(inputlst) % 2 != 0:
        f = len(inputlst) // 2 + 1
    else:
        f = len(inputlst) // 2
    flst = inputlst[:f]
    slst = inputlst[f:]

    printlst = []
    for i in range(len(slst)):
        printlst.append(flst[i])
        printlst.append(slst[i])
    if len(inputlst) %2 != 0:
        printlst.append(flst[-1])
    str = ' '.join(printlst)
    print(f'#{t} {str}')


