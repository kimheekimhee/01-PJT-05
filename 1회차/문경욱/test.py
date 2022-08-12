import sys

sys.stdin = open("_Flatten.txt")

for test_case in range(1, 11):
    # 덤프 시행 횟수
    dump_n = int(input())
    # 상자 높이
    list_ = list(map(int, input().split()))

    # 덤프를 더 이상 할 수 없을 때까지 반복
    while dump_n != -1:
        # max 값을 찾고
        max_ = max(list_)
        #print(f'max값 : {max_}')            
        # min값을 찾은 뒤
        min_ = min(list_)
        #print(f'min값 : {min_}')            
        # 둘의 차이를 구해서 새로운 변수에 저장 후
        gap_ = max_ - min_
        #print(f'gap_값 : {gap_}')            
        # 차 변수가 0 또는 1이면 종료
        if gap_ == 0 or gap_ == 1:
            break
        # 0또는 1이 아닌 경우 
        else:
            # 높이가 같을 경우 그 중 아무거나 옮길 수 있으므로 index를 활용해도 괜찮다.
            # max의 인덱스를 이용해 max -1, min의 인덱스를 이용해 min +1
         #   print(f'list_ max값 : {list_[list_.index(max_)]}')
          #  print(f'list_ min값 : {list_[list_.index(min_)]}')
            
            list_[list_.index(max_)] -= 1
            list_[list_.index(min_)] += 1
            

            # dump_n을 1 빼주고 반복
            dump_n -= 1

    # while문 다 돌고 난 후 test_case와 max - min을 출력
    print(f'#{test_case} {gap_}')

#print(list_)