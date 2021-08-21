# Greedy
> Is any algorithm that follows the problem-solving heuristic of making the locally optimal choice at each stage  
> 매 순간마다 최적으로 판단되는 선택을 이어나감으로써 최종 해답에 도달한다.

- 단, 일반적으로 locally optimized한 선택을 이어나갈 수 있지만 그게 globally optimized하다고 확신할 수는 없다.

### Greedy Choice Property
앞의 선택이 뒤에 영향을 주지 않는다는 보장이 필요하다. 

### Optimal Substructure
문제의 구조 적으로 최적화된 substructure을 가지고 있느냐 : 순간순간의 최적선택이 전체 문제의 최적화와 연관되었는가
- DP와도 관계있다. 갑자기 왜?
    - DP는 익숙해지면 코테를 걱정할 필요는 없다. 
    - Greedy는 문제가 요구하는걸 그대로 구현하면 되지만 DP는 점화식을 도출하는게 중요하기 때문
    - DP도 Optimal Substructure이라는 속성을 가지고 있다.

문제를 볼 때마다 반례가 있는지 생각해야 한다. 이게 최선인지 고민하자. (전체최선인지)

- 예제 : [5585](https://www.acmicpc.net/problem/5585)

### 대표적 예제
activity selection problem
- 최적으로 채워 넣는 방식
- 예제 : [회의실 배정](https://www.acmicpc.net/problem/1931)
huffman coding
- 압축을 구현 : 문자 압축, 데이터 압축 등 