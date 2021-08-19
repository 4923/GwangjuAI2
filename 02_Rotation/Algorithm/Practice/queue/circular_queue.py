# Queue

# - push X : 정수를 큐에 넣는 연산
# - pop : 큐에서 가장 앞에 있는 정수를 빼고 그 수를 **출력**, 비어있을 시 -1
# - size : 정수의 개수 출력
# - empty : 비어있으면 1 아니면 0
# - front : 가장 앞에 있는 값 **확인**, 비어있을 시 -1
# - back : 가장 뒤에 있는 값 **확인**, 비어있을 시 -1

# index based implement

import sys


class CircularQueue:
    def __init__(self, N):
        self.max = N
        self.queue = [None for _ in range(self.max)]
        self.front_idx = 0
        self.back_idx = 0

    def push(self, val: str):
        if self.is_full():
            return -1
        self.queue[self.back_idx % self.max] = int(val)
        self.back_idx += 1

    def pop(self):
        if self.is_empty():
            return -1
        pop_value = self.queue[self.front_idx % self.max]
        self.queue[self.front_idx % self.max] = None

        self.front_idx += 1
        return pop_value

    def size(self):
        return self.back_idx - self.front_idx

    def is_empty(self):
        if self.size() == 0:
            return 1
        return 0

    def is_full(self):
        if self.size() == self.max:
            return 1
        return 0

    def front(self):
        if self.is_empty():
            return -1
        return self.queue[self.front_idx % self.max]

    def back(self):
        if self.is_empty():
            return -1
        return self.queue[self.back_idx - 1 % self.max]


def main():
    # input
    print("How many commands do you have : ", end="")
    N, current = int(sys.stdin.readline().strip()), 0
    # instance
    Q = CircularQueue(N)
    # orders
    while current != N:
        command = sys.stdin.readline().strip().split()  # order, number
        cmd = command[0].lower()
        if cmd == "push":
            Q.push(int(command[1]))
        elif cmd == "pop":
            print(Q.pop())
        elif cmd == "size":
            print(Q.size())
        elif cmd == "empty":
            print(Q.is_empty())
        elif cmd == "front":
            print(Q.front())
        elif cmd == "back":
            print(Q.back())
        else:
            print("Wrong command. Try again")
            continue
        current += 1


if __name__ == "__main__":
    main()
