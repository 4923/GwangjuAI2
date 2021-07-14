# Queue

# - push X : 정수를 큐에 넣는 연산
# - pop : 큐에서 가장 앞에 있는 정수를 빼고 그 수를 **출력**, 비어있을 시 -1
# - size : 정수의 개수 출력
# - empty : 비어있으면 1 아니면 0
# - front : 가장 앞에 있는 값 **확인**, 비어있을 시 -1
# - back : 가장 뒤에 있는 값 **확인**, 비어있을 시 -1


import sys


class Queue:
    def __init__(self):
        self.queue = []
        self.queue_size = 0

    def push(self, val):
        self.queue.append(val)
        self.queue_size += 1

    def pop(self):
        if self.queue_size != 0:
            front_num, self.queue = self.queue[0], self.queue[1:]
            self.queue_size -= 1
            return front_num
        return -1

    def size(self):
        return self.queue_size

    def empty(self):
        if self.queue_size == 0:
            return 1
        return 0

    def front(self):
        if self.queue_size == 0:
            return -1
        return self.queue[0]

    def back(self):
        if self.queue_size == 0:
            return -1
        return self.queue[-1]


def main():
    # instance
    Q = Queue()
    # input
    print("How many commands do you have : ", end="")
    N, current = int(sys.stdin.readline().strip()), 0
    # orders
    while current != N:
        print("Your Command : ", end="")
        command = sys.stdin.readline().strip().split()  # order, number
        cmd = command[0].lower()
        if cmd == "push":
            Q.push(int(command[1]))
        elif cmd == "pop":
            print(Q.pop())
        elif cmd == "size":
            print(Q.size())
        elif cmd == "empty":
            print(Q.empty())
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
