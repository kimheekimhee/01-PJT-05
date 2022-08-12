import sys

sys.stdin = open("_반반.txt")
t = int(input())
for j in range(t):
    hash = {}
    s = input()
    for i in s:
        if i not in hash:
            hash[i] = 0
        if i in hash:
            hash[i] += 1
    try:
        x, y = hash.values()
    except:
        pass
    
    if len(hash) == 2 and x == 2 and y == 2:
        print(f'#{j + 1} Yes')
    else:
        print(f'#{j + 1} No')
