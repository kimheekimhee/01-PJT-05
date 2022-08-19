import sys

sys.stdin = open("_퍼펙트셔플.txt")

for test_case in range(1, int(input()) + 1):
    n = int(input())
    word = list(map(str, input().split()))
    # 카드가 짝수 인지 홀수 인지 파악 하기 위함
    k = n % 2
    # 짝수라면
    if not k:
        # 카드를 중앙값 기준으로 반반
        a = word[:n // 2]
        b = word[n // 2:]
        print(f'#{test_case}', end=" ")

        # 순서 대로 출력
        for i in range(len(a)):
            print(a[i], end=" ")
            print(b[i], end=" ")
    # 홀수라면
    else:
        # 중앙 값 기준으로 반으로 쪼개는데 a 라는곳에 하나더 추가!
        a = word[:len(word) // 2 + 1]
        b = word[len(word)// 2 + 1:]
        print(f"#{test_case}", end=" ")

        # a에는 b보다 한개더 많기 때문에 b의 길이 기준으로 출력
        for i in range(len(b)):
            print(a[i], end=" ")
            print(b[i], end=" ")
        # a에 마지막 하나 출력
        print(a[-1], end=" ")
    print()