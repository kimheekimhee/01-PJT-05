import sys

sys.stdin = open("_반반.txt")

TC =int(input())
for i in range(1,TC+1):
    S = input()
    if len(set(S)) == 2:
        print(f'#{i} Yes') 
    else:
        print(f'#{i} No')   