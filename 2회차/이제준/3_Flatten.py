import sys

sys.stdin = open("_Flatten.txt")

# import sys

# sys.stdin = open("input.txt")

for t in range(1, 11):

    C = int(input())
    area = list(map(int, input().split()))

    cnt = 0

    while cnt != C:
        tall = max(area)
        if len(set(area)) == 1:
            break
        else:
            for i in range(len(area)):
                if area[i] == tall:
                    area[i] = area[i] - 1
                    break
            
            short = min(area)                    
            for j in range(len(area)):
                if area[j] == short:
                    area[j] = area[j] + 1
                    cnt += 1
                    break
        
    result = max(area) - min(area)
    # print(area)
    # print(max(area), min(area))
    print(f'#{t} {result}')

