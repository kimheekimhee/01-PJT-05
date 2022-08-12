import sys

sys.stdin = open("_퍼펙트셔플.txt")

T = int(input())

for tc in range(T):
    N = int(input()) + 1 # 홀수개 슬라이싱 위함
    li = list(map(str,input().split()))
    #슬라이싱으로 반틈 나누기
    li1 = li[:(N//2)]
    li2 = li[(N//2):]
    ans = []
    for i in li1:
        for j in li2:
            if i not in ans:
                ans.append(i)
                if j not in ans:
                    ans.append(j)
                    break
            else:
                if j not in ans:
                    ans.append(j)
                    break
    print(f'#{tc+1} {" ".join(ans)}')