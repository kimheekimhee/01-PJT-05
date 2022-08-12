import sys

sys.stdin = open("_반반.txt")

T = int(input())

for t in range(1, T + 1):
    S = input()
    ban = {}
    answer = "No"
    # 조건을 만족하는 키의 수
    yes = 0
    for char in S:
        ban[char] = ban.get(char, 0) + 1
        
    for key in ban:
        if len(ban) != 2:
            continue
        
        if ban[key] == 2:
            yes += 1
            
    if yes == 2:
        answer = "Yes"
        
    print(f'#{t} {answer}')