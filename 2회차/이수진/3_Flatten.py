import sys
sys.stdin = open("_Flatten.txt")
for i in range(10):
    n=int(input())
    nums=list(map(int,input().split()))
    for _ in range(n):
        nums.sort()
        nums[0]+=1
        nums[-1]-=1
    nums.sort()
    print(f'#{i+1} {nums[-1]-nums[0]}')
        