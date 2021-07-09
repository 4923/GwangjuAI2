def run_cmd_with_stack(cmd, stack):
    cmd_type = cmd[0]
    # cmd_type, num = cmd

    if cmd_type == "push":
        _, num = cmd  # num = cmd[1]
        stack.append(num)
    elif cmd_type == "pop":
        if len(stack) > 0:
            print(stack.pop())
        else:
            print(-1)

        # try:
        #     print(stack.pop())
        # except IndexError:
        #     print(-1)
    elif cmd_type == "size":
        print(len(stack))
    elif cmd_type == "empty":
        if len(stack) > 0:
            print(0)
        else:
            print(1)
    elif cmd_type == "top":
        if len(stack) > 0:
            print(stack[-1])
        else:
            print(-1)

    return stack


n = int(input())
stack = []

for _ in range(n):
    # "push 2".split() => ["push", "2"]
    # "size".split() => ["size"]
    command = input().split()
    stack = run_cmd_with_stack(command, stack)

    # result = run_cmd_with_stack(command, stack)

    # if result is not None:
    #     stack = result
