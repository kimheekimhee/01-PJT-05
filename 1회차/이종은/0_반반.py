import sys
sys.stdin = open("_반반.txt")


t = int(input())

for _ in range(t):
    s = list(input())

    
    cnt = 0

    for i in s:
        
        if s.count(i) == 2:
            cnt = 1
        else:
            cnt = 0
            break

    if cnt == 1:
        print(f'#{_+1} {"Yes"}')
    else:
        print(f'#{_+1} {"No"}')


    




# ['ABAB', 'CCDD', 'EFFE', 'EEEE', 'NONE']