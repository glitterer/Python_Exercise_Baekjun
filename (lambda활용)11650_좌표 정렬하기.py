import sys
num = int(sys.stdin.readline())
arr = []
for _ in range(num):
    arr.append(list(map(int, sys.stdin.readline().split())))  #map 개념 제대로 알자
arr.sort(key=lambda x: (x[0], x[1])) #lambda에 대해서 제대로 알고 있자...
# print(arr)
for i in arr:
    print(i[0], i[1])
