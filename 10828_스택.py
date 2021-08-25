import sys
num = int(sys.stdin.readline())
stack = []
i = 0
for i in range(num):
    stack_word = sys.stdin.readline()
    if stack_word[:4] == "push":
        stack.append(int(stack_word[5:]))
    if stack_word[:3] == "pop":
        if len(stack) != 0:
            print(stack.pop())
        else:
            print(len(stack) - 1)
    elif stack_word[:4] == "size":
        print(len(stack))
    elif stack_word[:5] == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif stack_word[:3] == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
    else:
        pass
    i += 1
