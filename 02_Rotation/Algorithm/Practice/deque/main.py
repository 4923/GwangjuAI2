from collections import deque

# 에서 deque를 가져올 수 있다.

deque_obj = deque()
# deque로 덱을 사용할 수 있다.

print(deque_obj)
print(type(deque_obj))

# deque([])
# <class 'collections.deque'>

# append
deque_obj.append(10)
print(deque_obj)
deque_obj.append(20)
print(deque_obj)
deque_obj.appendleft(30)
print(deque_obj)
deque_obj.appendleft(40)
print(deque_obj)

# deque([10])
# deque([10, 20])
# deque([30, 10, 20])
# deque([40, 30, 10, 20])

# pop
deque_obj.pop()
print(deque_obj)
deque_obj.pop()
print(deque_obj)
deque_obj.popleft()
print(deque_obj)
deque_obj.popleft()
print(deque_obj)

# deque([40, 30, 10])
# deque([40, 30])
# deque([30])
# deque([])
