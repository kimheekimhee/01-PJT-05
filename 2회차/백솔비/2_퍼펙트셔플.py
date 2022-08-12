import sys
sys.stdin = open("_퍼펙트셔플.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cards = list(input().split())

    if N % 2 == 0:
        left = cards[:N//2]
        right = cards[N//2:N+1]
    else:
      left = cards[:N//2+1]
      right = cards[N//2+1:N+1]
    
    result = []
    while len(right):
        result.append(left[0])
        left.pop(0)
        result.append(right[0])
        right.pop(0)
    
    if left:
        result.append(left[0])
        left.pop(0)
    
    print(f'#{tc}', *result)