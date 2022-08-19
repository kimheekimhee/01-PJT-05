import sys
import math

sys.stdin = open("_퍼펙트셔플.txt")

for num in range(1, int(input())+1) :
    n = int(input())
    word = list(input().split())

    one = word[:math.ceil(n/2)]
    two = word[math.ceil(n/2):]

    perfect = []

    if len(one) == len(two) :
    
        for i in range(len(one)) :
            perfect.append(one[i])
            perfect.append(two[i])
        
    else :
        for i in range(min(len(one), len(two))) :
            perfect.append(one[i])
            perfect.append(two[i])
        perfect.append(one[-1])
                      
    print(f'#{num}', *perfect)