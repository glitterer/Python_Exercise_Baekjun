num = list(map(int, input().split()))
sum = 0
for i in num: #range(num)으로 하는 바람에 계속 틀림... 햇갈리지 말자
	sum = i**2 + sum
	# print(sum)
print(sum%10)
