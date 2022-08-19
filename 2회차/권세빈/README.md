## 후기 작성

### 각 문제별 다른 풀이 (필기노트 확인 or 구글링) 및 느낀점

- **0번**

  - `count 함수`를 깜빡했다! 더 간단하게 풀 수 있었는데 아쉽다.

  ```python
  T = int(input())
  for t in range(1,T+1):
      s = input()
      # 문자 판별용
      flg = True
  
      # 문자 하나씩 확인해볼때
      for i in s:
          # 만약 문자열 안에서 해당 문자가 딱 2개라면
          if s.count(i) == 2:
              # 무시하고 진행하기
              continue
          else:
              # 아니라면 플래그를 False로 바꾸고 멈추기
              flg = False
              break
          
      # 만약 플래그가 True라면 Yes 출력
      if flg:    
          print(f'#{t} Yes')
      else:
          # 아니라면 No 출력
          print(f'#{t} No')
  ```

  <br>

- **1번**

  - `replace 함수`를 굳이 쓰지 않아도 되는 문제였다..!

  ```python
  T = int(input())
  m = 'aeiou'
  for t in range(1,T+1):
      # 결과값 넣을 변수
      result = ''
      s = input()
      # 문자 확인
      for i in s:
          # 해당 문자가 모음에 속하지 않으면
          if i not in m:
              # 결과값에 추가
              result += i
      print(f'#{t} {result}')
  ```

  <br>

- **2번**

  - `while문`으로도 풀 수 있는 문제였다.

  ```python
  T = int(input())
  for t in range(1,T+1):
      n = int(input()) # 카드 개수
      card = input().split() # 카드들
      shuf = [] # 셔플 했을 때의 카드들
      
      # 슬라이싱으로 절반을 각각 new1, new2에 넣기
      if n % 2 == 0:
          new1 = card[:n//2]
          new2 = card[n//2:]
      else: # 홀수라면 +1해서 넣기
          new1 = card[:n//2+1]
          new2 = card[n//2+1:]
      
      # new1이나 new2에 카드가 있다면 계속 반복하기
      while new1 or new2:
          # 만약 new1가 비어있지 않다면 (True라면)
          if new1:
              # new1의 첫번째를 꺼내서 셔플에 넣기
              shuf.append(new1.pop(0))
              
          # new2도 똑같이 해줌
          if new2:
              shuf.append(new2.pop(0))
  
      print(f'#{t}', *shuf)
  ```

  <br>

- **3번**

  - `2차원 배열`을 이용해서 푸는 문제 같지만... 그렇게 풀지 못해서 아쉽다..ㅠ

- **4번**

  - `dfs 알고리즘`을 제대로 활용해서 뿌듯하다..!!

- **5번**

  - 5번 문제는 열심히 읽고나서 다른 문제를 풀었다ㅎ

<br>

### 전반적인 후기

- 그래도 가장 어려운 문제 빼고 모두 풀어서 뿌듯했다!!😆

  더 효율적인 방법을 생각 못한건 여전히 아쉽다.

- 그리고 2차원 배열.. 아직도 익숙하지가 않다ㅠ 

  열심히 계속해서 문제를 풀어야겠다!!