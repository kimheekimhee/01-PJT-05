import sys

sys.stdin = open("_퍼펙트셔플.txt")
t = int(input())
for i in range(t):
    n = int(input())
    lst = input().split()
    l_stk = lst[0:(n + 1)//2] # 리스트를 반 반으로 나누어줌
    r_stk = lst[(n + 1)//2:]
    
    res = []
    while l_stk or r_stk: 
        if len(l_stk) < 1: 
            continue
        else:
            res.append(l_stk.pop(0))
        if len(r_stk) < 1:
            continue
        else:
            res.append(r_stk.pop(0))
    print(f'#{i + 1}', *res)