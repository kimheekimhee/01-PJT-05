## 후기
5번까지 30분정도 걸렷는데 등산로 조성 문제가 상당히 어려웠다. 특히 cnt 초기값을 잘못 설정해서 답이 1씩 밀린다던지, `graph[x][y] > graph[nx][ny] - k`와 같은 조건문을 `graph[x][y] - k < graph[nx][ny]` 처럼 잘못 쓴다던지 visited 초기화를 안해서 처음사이클만 잘돌아간다던지 하는 문제가 많았다.

아무래도 복잡한 문제일수록 처음에 제대로 설계를 안하면 코드 짜다가 중간중간 설계 수정을 하게되는데 이때 미처 수정을 못한 부분이 완성된 코드에서 말썽을 부리는 경우가 있는것 같다. 예전부터 문제를 급하게 푸는 경향이 있었는데, 처음에 로직 설계를 확실하게 해야 이런 잔실수를 줄일 수 있을듯. 좋은 건축물은 좋은 도면에서 나온다!! 대충 뇌코딩 하지말고 종이에 그리면서 짜는 버릇을 들여야겠다.

분명 이런 조언을 강사분들께서 미리 해주셧는데 역시 겪어보지않으면 귀에 안들어온다.