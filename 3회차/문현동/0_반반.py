import sys

sys.stdin = open("_반반.txt")

TC = int(input())

for test_case in range(1, TC + 1):
    S = input()
    
    ref = True
    
    for s in S: # 조건은 문자열 내의 어떤 하나의 문자 개수가 4개가 안되어야 하고 그 문자는 짝수개 여야 한다.
        if S.count(s) != 4 and S.count(s) % 2 == 0:
            pass
        else:
            ref = False
    
    if ref == True:
        print(f"#{test_case} Yes")
    else:
        print(f"#{test_case} No")