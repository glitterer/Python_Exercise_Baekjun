num = int(input())
i = 0
prevNum = 1
while True:
    if num > prevNum + 6 * i:
        prevNum += 6 * i
        i += 1
    else:
        print(1 + i)
        break
