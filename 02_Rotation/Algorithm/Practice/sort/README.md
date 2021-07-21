# Sort

## 정렬의 종류 : [참고](https://www.youtube.com/watch?v=kPRA0W1kECg)
- 삽입정렬
- 선택정렬
- 버블정렬


## 시간복잡도
-|최선|최악|평균
-|-|-|-
삽입정렬| $N$ | $N^{2}$ | $N^{2}$
선택정렬|$N^{2}$ | $N^{2}$ | $N^{2}$
버블정렬|$N$ | $N^{2}$ | $N^{2}$


맨 끝에 도달할 때 까지 가거나 나보다 작은 값을 만날 때 까지 가기

- 왜 삽입정렬의 최선이 $N$인가?
    - 이미 정렬된 경우가 최선의 경우이기 때문
    - 단 하나도 스왑이 없을 경우 == 이미 정렬된 배열이다. 
        - -> 한번 갔다가 더 이상 아무것도 하지 않아도 된다.

## 버블정렬
느리다.