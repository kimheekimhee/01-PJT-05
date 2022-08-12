import sys

sys.stdin = open("_퍼펙트셔플.txt")
# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

# 각 테스트 케이스의 첫 번째 줄에는 자연수 N(1 ≤ N ≤ 1,000)이 주어진다.

# 두 번째 줄에는 덱에 카드가 놓인 순서대로 N개의 
# 카드 이름이 공백으로 구분되어 주어진다.

# 카드의 이름은 알파벳 대문자와 ‘-’만으로 이루어져 있으며, 
# 길이는 80이하이다.

for _ in range(1,1+int(input())):
    n = int(input())
    st = input().split()
    # print(st)

    ans = []
    if n % 2 == 0:
        first = (st[:n//2])
        secon = (st[n//2:])

        for a in range(n//2): # 전체길이 반절
            
            ans.append(first[a])
            ans.append(secon[a]) # n이 짝수일때 마무리

    else:
        # 두 길이중 더 긴 애를 하나  pop해서 나중에 뒤에 넣을까
        first = (st[:n//2+1])
        secon = (st[n//2+1:])
        if len(first) > len(secon):
            space = first.pop()
        else:
            space = secon.pop()
        # print(first,secon)
        for a in range(n//2): # 전체길이 반절
            
            ans.append(first[a])
            ans.append(secon[a])
        ans.append(space)
        # print(ans)
    ans = ' '.join(ans)
    print(f'#{_} {ans}')
#1 A D B E C F

