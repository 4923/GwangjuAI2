# https://www.acmicpc.net/problem/1021

from collections import deque

N, _ = map(int, input().split())
numbers = map(int, input().split())
Q = deque([i + 1 for i in range(N)])

cnt = 0
for number in numbers:
    idx = Q.index(number)
    if Q[0] == number:
        pass
    elif idx < len(Q) / 2:
        Q.rotate(-idx)
    else:
        idx = len(Q) - idx
        Q.rotate(idx)
    cnt += idx
    Q.popleft()

print(cnt)
