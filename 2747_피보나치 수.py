n = int(input())
res = [0]*(n+1)

for i in range(n+1):
    if i == 0:
        res[i] = 0
    elif i == 1:
        res[i] = 1
    else:
        res[i] = res[i-1] + res[i-2]
print(res[n])
# print(res)

