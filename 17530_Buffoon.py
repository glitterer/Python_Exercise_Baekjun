N = int(input())
# V = [0*i for i in range(N)] # 더 좋은 list 초기화 방법 = [0]*N으로 한다.
V = [0]*N
for i in range(N):
    V[i] = int(input())
    # print(V[i])
for j in range(N):
    if V[0] != max(int(V[0]), int(V[j])):
       res = 'N'
       break;
    else:
        res = 'S'
print(res)
