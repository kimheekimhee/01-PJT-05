T = 10

for i in range(1, T + 1):
    dump = int(input())

    h = list(map(int, input().split()))
    
    # 정말 단순하게 생각해서 풀었지만
    # 효율적이지 않는 것 같다.
    for _ in range(dump):
        h.sort()
        h[0] += 1
        h[-1] -= 1
    
    h.sort()
    
    print(f"#{i}", h[-1] - h[0])