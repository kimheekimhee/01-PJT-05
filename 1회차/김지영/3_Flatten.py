# 가장 높은 곳 상자를
# 가장 낮은 곳으로 옮기는게 dump +1
# 가장 높은 곳 - 가장 낮은곳

# T = 10
# input dump_count
# input height_list
# output = 최고점 - 최저점
import sys
sys.stdin = open("_Flatten.txt")

T = 10
for test_case in range(1,T+1):
    dump = int(input())
    height_list = list(map(int,input().split()))
    # print(height_list)
    for _ in range(dump):
        if max(height_list) == min(height_list):
            print('even')
            break
        if max(height_list) - min(height_list) == 1:
            print('odd')
            break
        mxh = max(height_list)
        mnh = min(height_list)
        # print(mxh,mnh)
        mxhidx = height_list.index(mxh)
        mnhidx = height_list.index(mnh)
        # print('index',mxhidx,mnhidx)
        height_list[mxhidx] = mxh - 1
        height_list[mnhidx] = mnh + 1
        # print(mxh,mnh)
    result = max(height_list) - min(height_list)
    print(f'#{test_case} {result}')