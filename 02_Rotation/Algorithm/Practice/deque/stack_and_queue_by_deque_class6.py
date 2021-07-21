from collections import deque

class StackAndQueue:
    def __init__(self, data_type="stack"):
        self.array = deque()
        self.data_type = data_type

    def push(self, num):
        self.array.append(num)

    def pop(self):
        if self.is_empty():
            return -1

        if self.is_stack():
            return self.array.pop()

        return self.array.popleft()

    def size(self):
        return len(self.array)

    def empty(self):
        return int(self.is_empty())

    def top(self):
        if not self.is_stack() or self.is_empty():
            return -1

        return self.array[-1]

    def front(self):
        if self.is_stack() or self.is_empty():
            return -1

        return self.array[0]

    def back(self):
        if self.is_stack() or self.is_empty():
            return -1

        return self.array[-1]
        # return self.get_last_val()

    # def get_last_val(self):
    #     return self.array[-1]

    def is_stack(self):
        return self.data_type == "stack"

    def is_empty(self):
        return self.size() == 0

def run_cmd(command, data_obj):
    cmd_type = command[0]

    if cmd_type == "push":
        _, num = command
        data_obj.push(num)
    
    elif cmd_type == "pop":
        print(data_obj.pop())

    elif cmd_type == "empty":
        print(data_obj.empty())

    elif cmd_type == "size":
        print(data_obj.size())
        
    elif cmd_type == "top":
        print(data_obj.top())

    elif cmd_type == "front":
        print(data_obj.front())
        
    elif cmd_type == "back":
        print(data_obj.back())

data_type = input() # "stack"
n = int(input())
data_obj = StackAndQueue(data_type)

for _ in range(n):
    run_cmd(input().split(), data_obj)