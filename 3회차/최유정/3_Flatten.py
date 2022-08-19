import sys

sys.stdin = open("_Flatten.txt")


for i in range(1, 11):
    T = int(input())
    inputlst = list(map(int,input().split()))

    for t in range(T+1):
        max_ = max(inputlst)
        min_ = min(inputlst)
        inputlst[inputlst.index(min_)] = min_ + 1
        inputlst[inputlst.index(max_)] = max_ - 1
    
    print(f'#{i} {max_ - min_}')