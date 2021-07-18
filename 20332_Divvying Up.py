contest_num = int(input())
prize = list(map(int, input().split()))
sum = 0
for i in range(contest_num):
    sum = sum + prize[i]
if sum % 3 != 0:
    print("no")
else:
    print("yes")
