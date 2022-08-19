import sys

sys.stdin = open("_반반.txt")
T = int(input())
for tc in range(1, T + 1):
    # 단어를 리스트로 만들어줌.
    word = input()
    # 각 단어에 중복이 몇개인지 카운트해줌
    cnt = [0] * 4
    # 4번씩 word를 반복
    for i in range(4):
        for j in word:
            # a가 abab의 0번째와 같다면 +1
            if j == word[i]:
                cnt[i] += 1
    # 모두 더했을때 8이 나와야 중복이 2개씩인것 같음
    if sum(cnt) == 8:
        print(f'#{tc} Yes')
    else:
        print(f'#{tc} No')