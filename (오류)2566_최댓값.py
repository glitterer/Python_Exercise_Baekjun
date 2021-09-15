arr = []
for i in range(9):
    arr.append(list(map(int, input().split())))
prevNum = arr[0][0]
for i in range(9):
    for j in range(9):
        maxNum = max(prevNum, arr[i][j])
        
        if maxNum != prevNum:
            i_num = i
            j_num = j
print(maxNum)
print(max(arr))
print(i_num+1, j_num+1)
