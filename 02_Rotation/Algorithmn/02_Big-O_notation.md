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

### 리스트의 함수와 시간복잡도
|동작|함수|Big-O|보충|
|-|-|-|-|
|indexing | `li[i]` | O(1)|해당하는 위치의 값을 불러온다. 리스트는 순차적 자료 구조이므로 **메모리 주소**를 **한번의 연산**으로 찾아갈 수 있다.
|store, assign| `li[i] = 10` | O(1)| 배열의 길이에 좌우되는 연산이 아니다.|
|length| `len(li)` | O{1) | 내부적으로 관리하고 있다. `li.__len__()`에 저장되어있기 때문에 이미 저장한 값을 불러오기만 하면 된다.
|append|`li.append(5)`| O(1) | 마지막 위치로 이동하여 대입 (indexing, store)|
|pop|`li.pop()`|O(1) | 마지막 위치의 값을 추출하는 것이므로 상수시간|
|clear|`li.clear()`|O(1)| 빈 리스트를 덮어씌운다. 대입연산과 동일. `li = []`|
|slice|`li[a:b]`|O(b-a)|
|extend|`li.extend(...)`|O(len(...)| `==concatnation` 특정 리스트 위에 다른 리스트를 추가하는 과정. 원본 리스트의 길이는 중요하지 않다. (마지막 위치로 이동하면 되므로) 하지만 그 이후에 추가하려는 리스트의 원소를 하나하나 append 하는 과정과 같다.|
|construction|`list(...)`|O(len(...))| extend와 마찬가지로 원소 하나하를 append 한다고 생각하면 된다. list뿐 아니라 순차적 자료구조 모두를 포함한다.|
|check ==, !=|`li1 == li2`|O(N)|모든 원소를 비교해야 하므로 입력값과 같은 N만큼 비교를 해야한다. (메모리 주소까지 동일한지 아닌지 확인하는 명령어는 `is` 이고 메모리주소만 확인하므로 O(1)이다.) |
|insert|`li.insert(i,v)`|O(N)|최악의 경우 이므로, 맨 처음 값에 insert하게 될 경우 첫 위치에 삽입하고 나머지 값을 이동해야 하므로 O(N)이다.|
|delete|`del li[i]`|O(N)|insert와 마찬가지로 맨 앞의 값을 삭제했을 경우 나머지 값을 하나씩 당겨야 하므로 최악의 경우 O(N)이다.|
|containment|`x in li`|O(N)|첫 위치부터 탐색하는데, 최악의 경우 마지막 값까지 비교해야 하므로 O(N)이다.|
|copy|`li.copy()`, `li[:]`|O(N)|shallow copy, list의 모든 값을 복사해서 새로 만들어야 하므로 O(N)|
|remove|`li.remove(...)`|O(N)|값을 찾고 다 당겨와야 하므로 del 연산과 같다.|
|pop|`li.pop(i)`|O(N)|parameter가 존재하는 pop. 최악의 경우는 `li.pop(0)`이며 시간복잡도는 O(N)이다.|
|extreme value|`min(li)`, `max(li)`|O(N)|n번 순회하여 가지고 있는 값보다 큰지 작은지 확인하는 탐색이므로 O(N), 정렬이 보장되지 않는 경우에서 N번 이하의 탐색을 할 수 있는 방법은 없다.|
|reverse|`li.reverse()`|O(N)|li의 맨 뒤에서부터 앞으로 값을 하나하나 가져와야 하므로 O(N)|
|iteration|`for v in li`|O(N)|모든 원소를 탐색하는 함수|
|sort|`li.sort()`|O(N log N)| 정렬 알고리즘에서 보충|
|multiply|`k*li`|O(k N)|크기를 k배 늘린다. ex) [0, 1, 2, 3, 4] * 5 => O(N**2 = 5 * 5)


- mutable variable vs immutable variable
    - Python의 자료형은 두가지 형태 : mutable, immutable 으로 분류 가능하다.
        - immutable : 숫자, 문자, boolean 등 변경 불가능한 자료형
            - Q) 숫자, 문자 모두 변경 가능하지 않나?
                - var = 123 처럼 변수를 선언하면 메모리 주소가 할당된다. 이 때 var = 456처럼 값을 변경할 경우 변수 var가 123이 아닌 456의 메모리 주소를 가리키게 된다. 즉, 값을 변경하기 전의 var과 변경한 후의 var은 완전히 다른 값이다.
        - mutable : list, dictionary 등 변경 가능한 자료형
            - append, pop 등의 함수를 사용해도 메모리 주소가 변하지 않는다.
        - <details>
            <summary>code example</summary>
            <img alt = "copy memory id check" src = img/copy_id.png>
            </details>
- 얕은 복사, 깊은 복사 [document](https://docs.python.org/ko/3/library/copy.html#:~:text=%EC%96%95%EC%9D%80%20%EB%B3%B5%EC%82%AC%EB%8A%94%20%EC%83%88%EB%A1%9C%EC%9A%B4%20%EB%B3%B5%ED%95%A9,%EB%B3%B5%ED%95%A9%20%EA%B0%9D%EC%B2%B4%EC%97%90%20%EC%82%BD%EC%9E%85%ED%95%A9%EB%8B%88%EB%8B%A4.)
    - 얕은 복사 
        - 값들을 가지고 새로 객체를 만들 때 사용하며 원래의 값에 영향을 미치지 않는다.
        - 방법
            1. li.copy()
            2. li[2:4]
        - 문제 : list만 복사하고, 그 안의 값은 참조한다.
    - 깊은 복사
        - 메모리 주소를 기준으로 복사가 진행된다.
        - 얕은 복사의 문제를 해결하기 위한 방법이다.
        - 얕은 복사와 같은 한 겹의 복사가 아닌 재귀적으로 전체를 복사하는 복사방법이다.
        - 복사 대상과는 다르게 전혀 다른 객체가 생성된다.


### 공간복잡도는?
시간 복잡도는 효율과 직결되는 영역이지만 python에서 메모리를 초과하는 경우가 자주 발생하지는 않는다. 
- 공간복잡도란? : space complexity는 프로그램을 실행하거나 출력결과를 발생하는 알고리즘에 대하여 알고리즘이 필요로하는 메모리 공간이다.

---
- 시간 복잡도를 정리한 노트가 있어서 첨부한다.
- [@4923 TIL/timeComplexity](https://github.com/4923/TIL/blob/master/Algorithm/timeComplexity.md)