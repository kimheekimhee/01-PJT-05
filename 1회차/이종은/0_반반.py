import sys
sys.stdin = open("_반반.txt")


t = int(input())

for _ in range(t):
    s = list(input())

    
    cnt = 0

    for i in s: # s에 문자열을 리스트로 받음
        
        if s.count(i) == 2: # s리스트에 s요소의 갯수를 확인하여 2개이면 cnt에 1을 추가
            cnt = 1 
        else: # 아니면 
            cnt = 0 # cnt를 0으로 초기화
            break 

    if cnt == 1:
        print(f'#{_+1} {"Yes"}')
    else:
        print(f'#{_+1} {"No"}')


    




# ['ABAB', 'CCDD', 'EFFE', 'EEEE', 'NONE']