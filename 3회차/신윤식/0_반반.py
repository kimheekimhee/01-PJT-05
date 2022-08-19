import sys
from collections import Counter
sys.stdin = open("./3회차/신윤식/_반반.txt")

T = int(input())

for _ in range(1, T+1):
    S = input()
    
    for i in sorted(Counter(S).items(),key=lambda x:-x[1]):
        
        if i[1] == 2:
            a = 1
        else:
            a = 0
    
    if a == 1:
        print(f'#{_} Yes')
    else:
        print(f'#{_} No')