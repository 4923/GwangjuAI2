class Queue:
    def __init__(self, n):
        # self.array = [None] * n
        self.array = [None for _ in range(n)]
        self.f_idx = 0
        self.b_idx = 0
    
    def push(self, num):
        self.array[self.b_idx] = num
        self.b_idx += 1

    def pop(self):
        # if self.f_idx == self.b_idx:
        # if self.b_idx - self.f_idx == 0:
        # if self.size() == 0:
        if self.is_empty():
            return -1

        pop_val = self.array[self.f_idx]
        self.f_idx += 1
        return pop_val

        # self.f_idx += 1
        # return self.array[self.f_idx-1]

    def size(self):
        return self.b_idx - self.f_idx

    def empty(self):
        return int(self.is_empty())

    def is_empty(self):
        return self.size() == 0

    def front(self):
        if self.is_empty():
            return -1

        return self.array[self.f_idx]

    def back(self):
        if self.is_empty():
            return -1

        return self.array[self.b_idx-1]

def run_cmd_with_queue(command, queue_obj):
# def runCmdWithQueue(command, queueObj):
    cmd_type = command[0]

    if cmd_type == "push":
        _, num = command
        queue_obj.push(int(num))

    elif cmd_type == "pop":
        print(queue_obj.pop())

    elif cmd_type == "size":
        print(queue_obj.size())

    elif cmd_type == "empty":
        print(queue_obj.empty())

    elif cmd_type == "front":
        print(queue_obj.front())
    
    elif cmd_type == "back":
        print(queue_obj.back())

n = int(input())
queue_obj = Queue(n)

for _ in range(n):
    run_cmd_with_queue(input().split(), queue_obj)