
import sys

sys.stdin = open("_퍼펙트셔플.txt")


from collections import deque


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):


    n= int(input())
    word =list(input().split())


    o=deque()
    t=deque()
    a= n- int(n/2)

    cnt= 0
    for w in word:
        cnt+=1
        if cnt<=a:
            o.append(w)
        else:
            t.append(w)

    result=[]
    cnt= 0
    for __ in range(n):
        cnt+=1
        if cnt%2==1:
            result.append(o.popleft())
        elif cnt%1==0:
            result.append(t.popleft())
    print(f'#{test_case} ',end='')
    print(*result)
