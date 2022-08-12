import sys

sys.stdin = open("_퍼펙트셔플.txt")


T = int(input())

for t in range(T):

    N = int(input())

    S_list = list(map(str,input().split()))

    if N%2 == 0:
        ans_index = int(N / 2)
    else:
        ans_index = int((N+1) / 2)

    front_list = S_list[:ans_index]
    back_list = S_list[ans_index:]

    # 짝수 N -2 /2 인덱스에서 짜름
    # 홀수 N-1 /2 인덱스에서 짜름

    ans_list = []
    back_index = 0
    for i in range(1,2*len(back_list),2):

        front_list.insert(i,back_list[back_index])
        back_index+=1

    print(f'#{t+1} {" ".join(front_list)}')
