# Quicksort

pivot 요소를 선택하고 그것을 기준으로 다른 요소를 분할한다. (pivot보다 큰 값과 작은 값) 또 이 과정을 재귀적으로 시행하여 정렬한다. 
- 제자리에서 수행 가능하다. : 별도의 메모리를 필요로 하지 않는다. (only small additional memory, 변수 몇개 정도)

## 단계
1. 임의의 pivot을 선택
2. Partitioning : 분할
    - 배열을 재배치 reorder
        - pivot보다 작은 값을 pivot 앞으로 오게끔 이동한다.
        - 큰 값은 뒤로 이동한다.
        - 같은 값은 앞으로 가도 뒤로 가도 상관 없다.
    - 예시
        1. 첫 값을 pivot이라고 했을 때 그 값을 제외한 두번째 값과 마지막값을 각각 front, rear라고 하고 pivot보다 큰 값을 찾을 때 까지 앞으로 (front) 작은 값을 찾을 때 까지 (rear) 인덱스를 이동한다.
        2. 1에서 찾은 pivot보다 큰 값과 작은 값을 교환하고 다시 front와 rear를 변경한다. (front의 index는 하나 크게, rear는 하나 작게)
        3. front와 rear의 순서가 바뀌어 rear의 index가 front보다 클 때 : 첫 값인 pivot과 rear의 위치를 바꾼다.
        4. 다시 첫 값을 pivot으로 설정하고 1로 돌아간다.
        5. 만약 값이 이미 정렬된 상황이라 (rear와 pivot이 같을때?) 면 pivot을 재설정한다.
        - front와 rear가 엇갈릴때 정렬된 subarray가 생겼다고 보는 듯
3. recursively apply, pivot 앞의 값이 하나가 될 때까지
    - 값이 하나일 때에는 이미 정렬되었다고 봐도 되기 때문

## 특징
1. 불안정정렬
    - 순서가 보장되지 않는다. 
    - 안정정렬 vs 불안정정렬 :  기준이 되는 값 외에도 다른 값도 정렬이 되어있는가
        - 시험성적으로 정렬했을 때 시험성적이 같은 학생들의 이름이 ㄱㄴㄷ순으로 정렬되어있다.
        - yes : 안정 (e.g 병합정렬)
        - no : 불안정 (e.g. quicksort)
2. 빠르다
    - wort-case performance : O(N^2)
    - Best-case performance : O(n log n)
3. 불균형분할
    - mergesort에서는 top down 방식이든 bottom up 방식이들 관계없이 규칙적인 크기로 값을 정렬했는데 quicksort는 pivot이 기준이기 때문에 균형적이지 않다.
4. pivot을 어떻게 구하나? : 대강 중앙값을 지정하는게 좋지만 이걸 위해 또 연산할 필요는 없다. subarray값이 하나 이하일 때 까지 정렬
