import sys

sys.stdin = open("_퍼펙트셔플.txt")

t = int(input())

for case in range(1, t+1):
    n = int(input())
    mun = list(input().split())
    if len(mun)%2 == 0:
        list_1=mun[:len(mun)//2]
        list_2=mun[len(mun)//2:]
    else:
        list_1=mun[:len(mun)//2+1]
        list_2=mun[len(mun)//2+1:]
    answer=[]
    while list_1 or list_2:
        if list_1:
            answer.append(list_1.pop(0))
        if list_2:
            answer.append(list_2.pop(0))
    print(f'#{case}', *answer)