import sys
input = sys.stdin.readline

nums = [list(input().rstrip()) for i in range(5)]

max_num = 0

for i in nums:
    if len(i) > max_num:
        max_num = len(i)

for i in range(max_num):
    for j in range(5):
        print(nums[j][i], end="")
