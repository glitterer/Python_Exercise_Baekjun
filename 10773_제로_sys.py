import sys
k = int(sys.stdin.readline())
num_list = []
for _ in range(k):
    num = int(sys.stdin.readline())
    if num != 0:
        num_list.append(num)
    else:
        num_list.pop()

total = 0
for i in num_list:
    total += i
print(total)
