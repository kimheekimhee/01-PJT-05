import sys

sys.stdin = open("_퍼펙트셔플.txt")


T = int(input())

for t in range(1, T+1) :
    n = int(input())
    card = list(input().split())

    if n %2 == 0 :
        dec1 = card[:int(n/2)]
        dec2 = card[int(n/2) :]
    else :
        dec1 = card[:int(n/2)+1]
        dec2 = card[int(n/2)+1 :]


    result = ''
    for i in range(n) :
        if i % 2 == 0 :
            result += dec1[i//2] + ' '
        else :
            result += dec2[i//2] + ' '

    print(f'#{t} {result}')