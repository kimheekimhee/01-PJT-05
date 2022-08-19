# 알파벳에서 모음은 ‘a’, ‘e’, ‘i’, ‘o’, ‘u’의 다섯가지로 예를 들어 “congratulation”이라는 단어를 당신이 보게 되면 “cngrtltn”으로 인식하게 될 것이다.


# [입력]

# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

# 각 테스트 케이스의 첫 번째 줄에는 길이가 50이하이고 알파벳 소문자만으로 이루어진 단어가 주어진다.
# 이 단어에 모음이 아닌 문자(자음)이 적어도 하나는 들어있다는 것이 보장된다.

# [출력]

# 테스트 케이스 T에 대한 결과는 “#T ”을 찍고,  각 테스트 케이스마다 주어진 단어를 당신이 어떻게 인식하는지를 출력한다.

import sys

sys.stdin = open("_모음이보이지않는사람.txt")

T = int(input())

# for문 사용 tc마다 입력받은 input값의 문자를 하나씩 확인한다.
for tc in range(1, T + 1) :
    data = input()
# result = 0으로 했더니 TypeError: unsupported operand type(s) for +=: 'int' and 'str' 출력돼서 ''로 넣어줌
    result = '' 
# data[i] 안에 모음이 있다면 continue하고, 자음일 경우에는 result에 문자를 추가한다.
    for i in range(len(data)) :
        if data[i] in ['a', 'e', 'i', 'o', 'u'] :
            continue
        result += data[i]
# 출력
    print('#%d %s' % (tc, result))
     



 



 
