import sys

sys.stdin = open("_퍼펙트셔플.txt")

T = int(input())
 
for tc in range(1,1+T):
    n = int(input())
    words = list(map(str,input().split()))
    median_num = n//2
    res = []
    idx = 1

    if n % 2 == 0:
 
        for q in range(n):
            if q < median_num:
                res.append(words[q])
            else:
                res.insert(idx,words[q])
                idx += 2
    else:
        for q in range(n):
            if q < median_num+1:
                res.append(words[q])
            else:
                res.insert(idx, words[q])
                idx += 2
 
print('#{}'.format(tc), *res)