# Queue

> 줄의 "뒤"로 가서 선다
> FIFO (First In First Out)

- 연산
    - pop() = dequeue()
    - push(val) = enqueue(val)
    - empty()
    - front(), rear()
        - stack의 top 대신 사용 : stack은 들어오는 방향과 나가는 방향이 동일하므로 top만 써도 괜찮았으나 queue는 다르다.
        - front : 앞의 값을 **확인** 
        - rear : back이라고도 한다. 맨 뒤에 있는 값을 **확인**한다.