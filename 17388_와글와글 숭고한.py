import sys
num = list(map(int, sys.stdin.readline().split()))
count = len(num)
total = 0
for i in num:
    total = total + i
if total >= 100:
    print("OK")
else:
    if min(num) == num[0]:
        print("Soongsil")
    elif min(num) == num[1]:
        print("Korea")
    else:
        print("Hanyang")
        
'''
a, b, c = map(int, input().split())
if a + b + c >= 100:
    print('OK')
else:
    if a<b and a<c:
        print('Soongsil')
    elif b<a and b<c:
        print('Korea')
    else:
        print('Hanyang')
'''
