import sys

sys.stdin = open("_Flatten.txt")


T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    dum= int(input())

    boxs = list(map(int,input().split()))


    for __ in range(dum):
        boxs[boxs.index(max(boxs))]-=1
        boxs[boxs.index(min(boxs))]+=1

    print(f'#{test_case} {max(boxs)-min(boxs)}')