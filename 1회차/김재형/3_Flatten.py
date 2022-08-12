import sys

sys.stdin = open("_Flatten.txt")



# dump 횟수
# 상자들의 높이

# max에서 하나빼고 min에 하나 더하고
T = 10
for t in range(T):
    dump = int(input())

    boxs = list(map(int, input().split()))


    while dump != 0:
        a = max(boxs) - 1
        b = min(boxs) + 1
        boxs.remove(max(boxs))
        boxs.remove(min(boxs))
        boxs.append(a)
        boxs.append(b)
        dump -= 1
    print(f'#{t+1} {max(boxs)-min(boxs)}')
