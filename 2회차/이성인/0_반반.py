import sys

sys.stdin = open("_반반.txt")
answer_list = []
N = int(input())
for _ in range(N):
    data = input()
    if len(set(data)) == 2: # 4글자 and 같은문자 2개는 무조건 문자2개이다. 
        answer_list.append("Yes")
    else:
        answer_list.append("No")
for n in range(1,N+1):
    print(f"#{n} {answer_list[n-1]}")