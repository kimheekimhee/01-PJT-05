import sys

sys.stdin = open("_퍼펙트셔플.txt")

# 카드 덱을 정확히 절반으로 나누고 나눈 것들에서 교대로 카드를 뽑아 새로운 덱을 만드는 것을 의미 

t = int(input())

for _ in range(t):
    n = int(input())
    data = list(input().split())

    if len(data) % 2 == 0:
        a = data[:len(data)//2] #[: 3]
        b = data[len(data)//2:] #[3:]

    else:
        a = data[:len(data) // 2+1]
        b = data[len(data) // 2+1 :]

    result = []

    while a or b:
        if a:
            result.append(a.pop(0))
        if b : 
            result.append(b.pop(0))
    
    print(f'#{_+1}', *result)
    
