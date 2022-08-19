import sys

sys.stdin = open("_반반.txt")

TC = int(input())
for tc in range(1, TC+1):
    dict = {}
    word = input()
    for char in word:
        if char not in dict:
            dict[char] = 1
        else:
            dict[char] += 1
    
    fail = 1
    
    if len(dict.keys()) != 2:
        fail = 0

    else:
        for i in dict.values():
            if i != 2:
                fail = 0
                break
    
    if fail == 0:
        print(f'#{tc} No')
    else:
        print(f'#{tc} Yes')
                
        