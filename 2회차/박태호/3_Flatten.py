import sys
 
sys.stdin = open("_Flatten.txt")
testcase = 10

for _ in range(1,1+testcase):
    dum = int(input())
    h = list(map(int,input().split()))
# print(h)

# print(min(h))
# print(h)
    while dum > 0 :
        dum -= 1
        
        max_i = h.index(max(h))
        max_n = h.pop(max_i)

        # print('인덱스:',max_i,min_i)
        # print(h)

        min_i = h.index(min(h))  # 최소값 인덱스 
        
        min_n = h.pop(min_i)    # 최소값을 뽑음
        
        # if max_n == min_n:
        # print('최대최소:',max_n,min_n)
        # print('#-------')
        max_n -= 1
        min_n += 1 # 최소값에 + 1

        h.append(max_n)
        h.append(min_n) # 다시 추가
         
    # print(max(h),min(h))
    print(f'#{_} {max(h)-min(h)}')