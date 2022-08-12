import sys

sys.stdin = open("_반반.txt")
S_list = []
T = int(input(sys.stdin))

for t in range(1,T+1):
    S = list(input())
    letters = list(set(S))

    check = True
    
    for i in letters:
        if S.count(i) != 2:
            check = False
    if check:
        print(f"#{t} Yes")
    else:
        print(f"#{t} No")




