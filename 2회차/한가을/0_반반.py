import sys

sys.stdin = open("_반반.txt")

# 길이 4의 알파벳 대문자로 이루어진 문자열 S가 주어졌을 때
# S에 정확히 두 개의 서로 다른 문자가 등장하고
# 각 문자가 정확히 두 번 등장하는지 판별

# 첫 번째 줄에 테스트 케이스의 수 TC가 주어진다
# 이후 TC개의 테스트 케이스가 새 줄로 주어진다
# 첫 번째 줄에 문자열 S가 주어진다

# 각 테스트 케이스마다 조건이 만족되면 Yes 아니면 No 출력

TC = int(input())

for k in range(1, TC + 1):
    S = list(input())

    result = 0

    for i in range(4):
        count = 0

        for j in range(4):
            if S[i] == S[j]:
                count += 1
        
        if count == 2:
            result += 1
    
    if result == 4:
        print('#{} {}'.format(k, 'Yes'))
    else:
        print('#{} {}'.format(k, 'No'))