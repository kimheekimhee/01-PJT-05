import sys

sys.stdin = open("_반반.txt")

N = int(input())



for i in range (1,N+1):
    string = input()
    temp1 = ''
    temp2 = ''
    
    for n in range(len(string)):
        if n == 0:
            temp1 += string[n]
            continue
        if string[n] in temp1:
            temp1 += string[n]
        else:
            temp2 += string[n]
    
    if not temp1 or not temp2:
        print(f'#{i} No')
    else:
        if temp1[0] == temp1[1] and temp2[0] == temp2[1]:
            print(f'#{i} Yes')
        else:
            print(f'#{i} No')
            
 


  