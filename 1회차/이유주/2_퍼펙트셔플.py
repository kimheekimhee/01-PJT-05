import sys

sys.stdin = open("_퍼펙트셔플.txt")

T = int(input()) #테스트케이스 수



for i in range(1, T+1):
    n = int(input()) #카드 수
    divide = [0] * n
    card = list(map(str, input().split()))
   

    #짝수일때
    if n % 2 == 0:
        for x in range(n//2):
            divide[x*2] = card[x]
            divide[(x*2)+1] = card[(n//2)+x]
        
    # #홀수일때
    if n % 2 == 1:
        for x in range(n//2+1):
            divide[x*2] = card[x]
        for x in range(n//2):
            divide[x*2+1] = card[(n//2)+1+x]
    print(f'#{i} {divide}')

