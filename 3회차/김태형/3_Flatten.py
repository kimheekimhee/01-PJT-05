# 횟수만큼 옮기는 작업을 한 후 최고점과 최저점의 차이를 반환하는 프로그램을 작성하시오.

import sys

sys.stdin = open("_Flatten.txt")

# 내림차순으로 정렬하면 최저점은 맨 앞, 최고점은 맨 뒤에 위치한다. 
# (heap은 완전한 정렬이 되지 않는다.)
# 평탄화 작업
for i in range(1,11):
    l = []
    n=int(input())
    l=list(map(int,input().split()))
    for j in range(n):
        l.sort()
        l.append(l.pop(99)-1)
        l.append(l.pop(0)+1)
        l.sort()
        h = l[99]-l[0]
        # 조건 : 평탄화가 완료되면
        if h==1 or h==0:
            break
    print(f"#{i} {h}")