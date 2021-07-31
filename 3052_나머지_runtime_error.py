#runtime error(IndexError)  ==> 반례가 있을 것으로 추정됨.
index = [0]*10
for i in range(10):
    num = int(input())
    index[i] = num % 42
index.sort()
# print(index, end = ' ')

cnt = 0
dif = 0
for i in index:
    if index[cnt] == index[cnt+1] and cnt != 10:
        index.remove(i)
        cnt += 1
    elif cnt != 0 and index[cnt-1] != index[cnt]:
        cnt += 1
if len(index) == 5:  # 5인 이유는 위의 for문에 의해 모두가 같은 숫자일 때 5개가 남기 때문이다.
    print(1)
else:
    # print(index)
    print(len(index))
