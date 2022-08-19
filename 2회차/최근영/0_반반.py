import sys

sys.stdin = open("_반반.txt")

T = int(sys.stdin.readline())

for i in range(1,T+1):
    dict = {}
    cnt = 0
    S = sys.stdin.readline()
    for j in S:
        if j in dict:
            dict[j] += 1
        else:
            dict[j] = 1
    
    for v in dict.values():
        if v == 2:
            cnt+=1
    if cnt == 2:
        print(f'#{i} Yes')
    else:
        print(f'#{i} No')