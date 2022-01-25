changeType = [500, 100, 50, 10, 5, 1]
Taro = int(input())
remain = 1000 - Taro
remain1 = 0
for i in changeType:
    remain1 = remain1 + (remain // i)
    remain = remain % i
print(remain1)
