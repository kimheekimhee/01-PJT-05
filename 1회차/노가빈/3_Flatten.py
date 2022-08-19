for i in range(10):
    dumpnum = int(input())
    dumplst = list(map(int,input().split()))
    for j in range(dumpnum):   
        maxnum = max(dumplst)
        minnum = min(dumplst)
        dumplst[dumplst.index(maxnum)] = dumplst[dumplst.index(maxnum)]-1
        dumplst[dumplst.index(minnum)] = dumplst[dumplst.index(minnum)]+1
    resultmax = max(dumplst)
    resultmin = min(dumplst)
    print(f'#{i+1} {resultmax-resultmin}')