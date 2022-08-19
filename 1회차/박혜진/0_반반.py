import sys

sys.stdin = open("_반반.txt")

for num in range(1, int(input())+1) :
    word = input()

    alpha = set()
    for i in word :
        alpha.add(i)
    
    if len(alpha) == 2 :
        ans = 'Yes'
    
    else :
        ans = 'No'

    print(f'#{num} {ans}')