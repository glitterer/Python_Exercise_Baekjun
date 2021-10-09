from itertools import combinations
num =  int(input())
nums = []
for i in range(1, num):
    nums.append(i)
# print(nums)
combis = list(combinations(nums, 3))
# print(combis)
print(len(combis))

'''
중요한 부분:
"The input will be the positive integer J (1 ≤ J ≤ 99), which is the jersey number of the goal scorer."
==>입력값은 마지막 선수라는 것!
'''
