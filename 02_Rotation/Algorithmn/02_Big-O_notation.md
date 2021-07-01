# 점근표기법 (Big-O notation)

<p align="center">
    <img src="img/time_complexity_chart.jpeg" alt="time-complexity-chart" width=600>
</p>

> 알고리즘을 몰라도 알고리즘 문제는 풀리긴 한다. 중요한건 **얼마나 빠르게 답을 구할 수 있는가**다.

> **최악의 경우** 연산한 횟수를 식으로 나타냈을 때 가장 높은 차수만 고려하는 방식이 점근표기법 또는 Big-O 표기법이다.

### 왜 중요한가?
**시간복잡도를 계산하는 이유는 계산 횟수를 어림짐작하기 위함이다.**
계산이 1억회 이상 시행되면 안된다. 천만 단위도 지양하는 편이 좋다.
O(N^2) 알고리즘에서도 계산 횟수가 천만 이하라면 그 방법으로 풀어도 상관 없다.  

### 각 시간복잡도 별 특징
- `N(1)`, `N(O)`로 해결되는 경우는 많지 않다.
- 가장 적절한 시간 복잡도는 보통 `N(nlogn)`에 가깝다.
    - 현실적으로 쓰이는 시간복잡도 묻는 문제가 있다? 80% 정도 `N(nlogn)` :laughing:


---
- 정리한 노트가 있어서 첨부한다.
- [@4923 TIL/timeComplexity](https://github.com/4923/TIL/blob/master/Algorithm/timeComplexity.md)