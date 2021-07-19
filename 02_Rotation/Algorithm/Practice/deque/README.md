# Deque

> Double Ended Queue

다른 값에 대해 일일히 n번만큼 작업하지 않도록 설계된 구조.

기본적으로 리스트를 생각하면 되나 pop, append에 소요되는 시간이 더 짧다.
list는 append나 pop을 하면 끝에서 추가와 삭제가 이루어지는데 deque는 popleft, appendleft ... 가 가능해 진다.  
따라서 시간복잡도는 모두 $O(1)$ 이다. 

```python
from collections import deque
# 에서 deque를 가져올 수 있다.

deque_obj = deque()
# deque로 덱을 사용할 수 있다.
```

별도의 언급이 없는 한 코딩테스트에서 deque 등을 사용할 수 있다. 
(내부 기본 모듈이기 때문)