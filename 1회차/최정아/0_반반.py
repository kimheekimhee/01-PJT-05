import sys
from pprint import pprint
sys.stdin = open("_반반.txt")


tc = str(input()) # 테스트 케이스의 수를 문자열로 변환
tc.sort() # sort 통해서 정렬
tc = int(input())

count = 1
for i in range(int(input())):
    if [0] == [0 + 1]: # 이어지는 문자가 같으면
        count += 1 # count에 1씩 증가
        continue
    if count == 2: # 2와 같으면
        print("Yes") # "Yes" 출력
    if count > 2:
        print("No")

