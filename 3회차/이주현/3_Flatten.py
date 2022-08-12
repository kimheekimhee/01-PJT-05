import sys

sys.stdin = open("_Flatten.txt")


for tc in range(1,11):
    N = int(input())
    blocks = list(map(int,input().split()))

    for n in range(N):
        
        tall = blocks[0]
        small = blocks[0]
        for block in blocks[1:]:
            if block > tall:
                tall = block
            if block < small:
                small = block

        for i in range(len(blocks)):
            if blocks[i] == tall:
                blocks[i] -= 1
                break
        for i in range(len(blocks)):
            if blocks[i] == small:
                blocks[i] += 1
                break

        tall = blocks[0]
        small = blocks[0]
        for block in blocks[1:]:
            if block > tall:
                tall = block
            if block < small:
                small = block

        if tall - small <= 1:
            break
    print('#{} {}'.format(tc,tall - small))