num = list(map(int, input().split()))
prize = 0
if num[0] == num[1] == num [2]:
    prize = 10000 + num[0]*1000
elif num[0] == num[1] or num[0] == num[2] or num[1] == num[2]:
    if num[0] == num[1] or num[0] == num[2]:
        prize = 1000 + num[0]*100
    else:
        prize = 1000 + num[1]*100
else:
    prize = max(num[0], num[1], num[2])*100
print(prize)
