a, b = input().split()

a = list(map(int, a))
b = list(map(int, b))
print(sum(a) * sum(b))


'''
import sys
a, b = map(str, sys.stdin.readline().split())
total = []
for i in a:
    for j in b:
        total.append(int(i)*int(j))
print(sum(total))
'''
