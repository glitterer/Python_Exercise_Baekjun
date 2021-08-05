A = int(input())
B = int(input())
C = int(input())
res = list(map(int, str(A*B*C)))  # 이 부분을 유의하자. int -> list로 바꾼다.
nums = [0]*10
for i in res:
    for j in range(10):
        if j == int(i):
            nums[j] += 1
for j in range(10):
    print(nums[j])
