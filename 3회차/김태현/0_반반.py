import sys
sys.stdin = open("_반반.txt")

# 조건1. 서로 다른 2개의 문자 -> len(set()) == 2
# 조건2. 각 문자가 2번씩 등장 -> list.count(i) for i in set()



T = int(input())

for t in range(1, T+1):
    
    
    word = input()
    # 성공 실패
    isBool = False
    # 조건1 불만족시 False
    if len(set(word)) == 2:
    # 조건2 불만족시 False
        for i in set(word):
            if word.count(i) == 2:
                isBool = True
    
    if isBool:
        print(f"#{t} Yes")
    else:
        print(f"#{t} No")