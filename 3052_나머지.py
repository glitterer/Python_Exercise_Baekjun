# 중복제거를 해주는 파이썬의 함수가 존재한다 ==> set()

arr = []
for i in range(10):
    n = int(input())
    arr.append(n % 42)
arr = set(arr)
print(len(arr))
