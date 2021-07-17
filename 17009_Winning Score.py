apple_total = 0
banana_total = 0
for score in [3, 2, 1]:
    apples = int(input())
    apple_total = apple_total + score*apples
for score in [3, 2, 1]:
    bananas = int(input())
    banana_total = banana_total + score*bananas

if apple_total > banana_total:
    print('A')
elif apple_total < banana_total:
    print('B')
else:
    print('T')

'''
arr=[]
for i in range(6):
  arr.append(int(input()))
d1 = arr[0]*3 + arr[1]*2 + arr[2]
d2 = arr[3]*3 + arr[4]*2 + arr[5]
s = "T"
if d1 > d2 : s = "A"
elif d1 < d2 : s = "B"
print(s)
'''
