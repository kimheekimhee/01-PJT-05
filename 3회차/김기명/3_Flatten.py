import sys

sys.stdin = open("_Flatten.txt")
from pprint import pprint
# 제한된 횟수의 평탄화를 하고나서 최고점 최저점 차이반환
# 가로 (열 갯수)는 100임.
# 행도 100임. 
# 덤프횟수 1~1000
# 숫자가 너무커서 테스트를 하기 힘든 문제같다...


# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 11):
    n = int(input())    # 덤프횟수

    list_ = [[0] * 100 for i in range(100)]               # 100 x 100 행렬
    height = list(map(int, input().split()))                #높이가 주어진것을 이용해서 list_[height[i]][i] ~ list_[100][i] 를 1로 채워야함... << 이렇게 하니까 안되는데 왜그럴까 (list_[j][i]로 하니까)

    for i in range(100):                                    #이상하게 출력되고 list_[i][j] = 1로하니까 정상적으로 출력됨.. 왜 되는지 잘모르겠음..
        for j in range(height[i], 100):
            list_[i][j] = 1
    list_sum = []           #세트를 쓰려고했으나 순서를 확인해야하는 상황이 있었음
    for i in list_:
        list_sum.append(sum(i)) 
    
    min_ = min(list_sum)
    max_ = max(list_sum)
    cnt = 0
    while cnt != n:
        max_i = 0
        min_i = 0
        # 조건 1. 평탄화가 끝났을때 (최대높이 - 최소높이가 1 혹은 0일때 --> 2라면 무조건 평탄화 더 할수있음)는 그냥 차이 출력후 끝냄
        if max_ - min_ == 1 or max_ - min_ == 0:
            print(f'#{test_case} {max_ - min_}')
            break
        

        for i in range(100):
            if list_sum[i] == max_:
                max_i = i
                list_sum.pop(i)       #합계리스트(상자높이 리스트)에서 최대, 최소치를 빼줘야 다음 while순회에서 다른 최대최소치를 뽑아올수있음 문제는 시간복잡도가 너무높은것 같음
                break
            elif list_sum[i] == min_:
                min_i = i
                list_sum.pop(i)
                break

        #list_[max_i]의 제일 높이 있는 1 [100 - max_]은 0으로 만들고 ,list_[min_i]에 제일높이있는 1 [100 - min_] 위를 1로 만든다.
        list_[max_i][100 - max_] = 0
        list_[min_i][100 - (min_ + 1)] = 1
        # list_[100 - max_][max_i] = 0
        # list_[100 - (min_ + 1)][min_i] = 1
        min_ = min(list_sum)
        max_ = max(list_sum)

        cnt += 1
    print(f'#{test_case} {max_ - min_}')                #어디서 틀렸는지 감도 안옴