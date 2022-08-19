import sys

sys.stdin = open("_Flatten.txt")

for i in range(1,11):
    
    N = int(sys.stdin.readline())
    block = list(map(int,sys.stdin.readline().split()))
    for j in range(N):
        cnt = 0
        for k in block:
            if k == min(block):
                block[cnt] += 1
                cnt = 0
                break
            cnt+=1
        for l in block:
            if l == max(block):
                block[cnt] -= 1
                cnt = 0
                break
            cnt+=1
    print(f"#{i}", max(block)-min(block))