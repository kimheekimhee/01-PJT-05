import sys

sys.stdin = open("_창용마을무리의개수.txt")

for num in range(1, int(input())+1) :
    n, m = map(int, input().split())

    group = []
    for _ in range(m) :
        rel = list(map(int, input().split()))
        group.append(rel)
    
    muri = []
    muri.append(set(group[0]))

    for i in range(len(muri)) :
        for j in range(len(group)) :
            if j+1 < len(group) :
                if group[j+1][0] in muri[i] :
                    muri[i].add(group[j+1][0])
                    muri[i].add(group[j+1][1])
                
                else :
                    muri.append(set(group[j+1]))

    muri_group = []
    for m in range(len(muri)-1) :
        for o in range(1, len(muri)) :
            for oo in muri[o] :
                if oo in muri[m] :
                    muri[m].add(muri[o])
                    muri_group.append(muri[m])

    print(muri)
    print(muri_group)
       


    # group = []
    # for _ in range(m) :
    #     rel = list(input().split())
    #     group.append(rel)

    # for i in range(len(group)) :
    #     if i+1 < len(group) :
    #        if group[i+1][0] in group[i] or group[i+1][1] in group[0] :
    #         group[0].append(group[i+1][0])
    #         group[0].append(group[i+1][1])
    #         group.remove(group[i+1])
           
           
            # if group[i+1] in group[i] :
            #     group[i].add(group[i+1])
            #     group.remove(group[i+1])

            
            # if group[i][1] == group[i+1][0] :
            #     group[i].append(group[i+1][1])
            #     group.remove(group[i+1])
    
