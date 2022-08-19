import sys

sys.stdin = open("_모음이보이지않는사람.txt")

t = int(input())
out = ['a','e','i','o','u']

for test_case in range(1, t + 1):
    word = list(input())
    result = []
    print(f'#{test_case}', end = ' ')
    for i in word:
        if i not in out:
            result.append(i)
    print(*result, sep = '')



# remove랑 pop이 제대로 작동하지 않습니다. 제가 뭘 잘못 사용하고 있나요?ㅠㅠ
t = int(input())
out = ['a','e','i','o','u']
for test_case in range(1, t + 1):
    word = list(input())
    for i in word:
        if i in out:
            word.remove(i)
    print(*word, sep = '')
# 이 코드를 돌리면, 제 생각에는 반복문 돌면서 다 제거되어야 하는데 
# c n g r t l t o n
# s y n t h t c
# f l i d
# 출력값이 이렇게 지저분하게 나옵니다...


for test_case in range(1, t + 1):
    word = list(input())
    for i in range(len(word)):
        if word[i] in out:
            word.pop(i)
    print(*word, sep = '')
# 이 코드는 인덱스 에러가 납니다.