# N개의 카드가 있는 덱이 주어질 때 이를 퍼펙트 셔플하면 어떤 순서가 되는지 출력하는 프로그램을 작성하라.

import sys

sys.stdin = open("_퍼펙트셔플.txt")

T = int(input())
for t in range(1,T+1):
    p_list = []
    N = int(input())
    l = input().split()
    # 퍼팩트 셔플 : 리스트를 반으로 나누고, 나눈 리스트에서 순서대로 다시 합친다.
    if N%2==0:
        l1 = l[0:(N//2)]
        l2 = l[(N//2):N]

        for i in range(N//2):
            p_list.append(l1[i])
            p_list.append(l2[i])
    # N이 홀수인 경우에는 첫번째 리스트에 요소를 하나 더 준다.
    else:
        l1 = l[0:((N//2)+1)]
        l2 = l[((N//2)+1):N]

        for i in range(N//2):
            p_list.append(l1[i])
            p_list.append(l2[i])
        p_list.append(l1[N//2]) # 순서대로 넣어주고 남은 첫번째 리스트의 요소를 넣어준다.
    p = " ".join(p_list)
    print(f"#{t} {p}")