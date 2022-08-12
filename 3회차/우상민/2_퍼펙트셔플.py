import sys

sys.stdin = open("_퍼펙트셔플.txt")

for T in range(1, int(input())+1):
    box = []
    total = []
    N = int(input())
    li = list((input().split()))
    S = N // 2
    if N % 2 == 0:
        for i in range(S):
            box.append(li[0])
            li.remove(li[0])
        for idx in range(S):
            total.append(box[idx])
            total.append(li[idx])
    elif N % 2 == 1:
        for i in range(S+1):
            box.append(li[0])
            li.remove(li[0])
        for idx in range(S):
            total.append(box[idx])
            total.append(li[idx])
        total.append(box[S])
    print(f'#{T}', *total)
            



