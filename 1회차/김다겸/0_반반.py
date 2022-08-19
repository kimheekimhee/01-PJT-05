import sys

sys.stdin = open("_반반.txt")

T = int(input())

for t in range(1, T+1):
    # 알파벳 인덱스로 저장할 리스트 생성
    list_s = [0] * 29
    s = input()
    cnt = 0

    for i in s:
        # 입력받은 문자열의 문자를 아스키코드 - 65로 바꾼 후 해당 인덱스에 1 더하기
        list_s[(ord(i)-65)] += 1
    for i in range(len(list_s)):
        # 결과가 2이면
        if list_s[i] == 2:
            # cnt에 1더하기
            cnt += 1
    # 알바벳 두개가 두번씩 나왔으면
    if cnt == 2:
        print(f'#{t} Yes')
    else:
        print(f'#{t} No')