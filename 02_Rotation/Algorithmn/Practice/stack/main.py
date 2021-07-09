import sys


class Stack:
    def __init__(self):
        self.stack = []
        self.leng = 0

    def push(self, value):
        self.stack.append(int(value))   # append만 value 값이 있으므로 int 처리 할 필요 O
        self.leng += 1

    def pop(self):
        if self.leng != 0:
            self.leng -= 1
            return self.stack.pop()
        return -1

    def size(self):
        return self.leng

    def empty(self):
        if self.leng == 0:
            return 1
        return 0

    def top(self):
        if self.leng != 0:
            return self.stack[-1]
        return -1


def main():
    S = Stack()

    print("How many commands do you have : ", end="")
    how_many = int(sys.stdin.readline().strip())
    cnt = 0
    while cnt != how_many:
        print("Your Command : ", end="")
        cmd = sys.stdin.readline().strip().split()

        if cmd[0] == "push":
            S.push(cmd[1])
            # print(cmd[1])
        elif cmd[0] == "pop":
            print(S.pop())
        elif cmd[0] == "size":
            print(S.size())
        elif cmd[0] == "empty":
            print(S.empty())
        elif cmd[0] == "top":
            print(S.top())
        else:
            print("Wrong Command. Try Again")
            continue
        cnt += 1


if __name__ == "__main__":
    main()
