import sys

sys.stdin = open("_Flatten.txt")

T = 10

for _ in range(1, T+1):
    N = int(input())
    row = list(map(int, input().split()))
    
    # print(row[37] -1)
    # print(row.index(max(row)))

    for i in range(N):      # sort후  제일 끝에있는 수를 조작
        row.sort()
        row[0] += 1
        row[len(row)-1] -= 1 
    
    print(f'#{_} {max(row) - min(row)}')  # 큰수에서 작은수 차이 구하기

'''
sort 하면서  제일 끝에있는 수를 조작해서 풀이했다. 
17번 수정 : 가로가 100 고정이라 처음엔 99를 넣었지만 가로가 늘어나도 괜찮게 바꿔봤습니다.

반복문을 돌 때마다 정렬한다는 점이 신경쓰입니다.
'''