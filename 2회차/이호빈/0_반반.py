import sys
from collections import Counter

sys.stdin = open("_반반.txt")

T = int(input())
# 결과 값을 비교하기 위한 변수 
answer = 2
#입력 받아주고
for tc in range(1, T+ 1):
    s = input()
    #Counter함수를 사용해서 각 요소의 개수를 찾아주고
    k = Counter(s)
    #딕셔너리의 value를 변수에 담아주고
    k_values = list(k.values())
    #count함수를 사용해서 2의 개수가 몇 개인지 파악한다. 그게 문제에서 요구하는 2개이면 값을 yes 아니면 no를 출력한다. 
    if k_values.count(answer) == 2:
        print(f"#{tc} Yes")
    else:
        print(f"#{tc} No")