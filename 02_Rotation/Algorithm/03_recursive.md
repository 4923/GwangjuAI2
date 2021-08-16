# recursive
> 재귀 : 자기 자신을 호출하는 것

- 퇴각검색법 backtracking과는 다르다.  재귀를 이용해 *탐색* 하는 것이기 때문에 재귀가 좀 더 큰 분류다.
- **동일한 구조의 "반복"** 으로 이해하자. 이 반복 안에 **자기 자신**이 들어가 있는 것을 재귀라고 한다.
- 무한한 반복을 피하기 위해 **종결조건** 또는 **탈출조건**을 지정한다.
- 어지간해선, 반복으로 풀리면 재귀로 풀리고 재귀로 풀리면 반복으로 풀린다. 
- 더 작은 인스턴스 단위로 쪼개지고 그 해결법이 동일한 문제를 구조에 의존하여 푼다 : 작은 단위의 규칙을 찾는다.

예시 문제
- 팩토리얼

call stack?