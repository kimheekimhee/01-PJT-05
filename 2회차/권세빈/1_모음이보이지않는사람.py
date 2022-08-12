import sys

sys.stdin = open("_모음이보이지않는사람.txt")

T = int(input())
m = 'aeiou'
for t in range(1,T+1):
    s = input()
    # 문자 확인
    for i in s:
        # 해당 문자가 모음에 속하면
        if i in m:
            # replace 함수로 공백 없는걸로 대체하고 재할당
            s = s.replace(i,'')
    print(f'#{t} {s}')