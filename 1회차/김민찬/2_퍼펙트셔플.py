import sys

sys.stdin = open("_퍼펙트셔플.txt")

T = int(input()) # 테스트 케이스의 수 T가 주어진다.
for i in range(1, T + 1):
    N = int(input()) # 자연수 N이 주어진다.
    word = list(map(str, input().split()))
    divide = N // 2 # 나뉘는 값 -> 2로 나눈다.
    li = [] # 저장 공간
    index = 1 # 위치 값

    if N % 2 == 0: # N의 값이 짝수일 경우
        for j in range(N):
            if j < divide:
                li.append(word[j])
            else:
                li.insert(index, word[j])
                index += 2
    else:
        for j in range(N):
            if j < divide + 1:
                li.append(word[j])
            else:
                li.insert(index, word[j])
                index += 2

    print('#{}'.format(i), *li) # [] 제거하기 위해 * 사용