def dnaTable(col, row):
    if col == 'A' and row == 'A':
        return 'A'
    if col == 'A' and row == 'G':
        return 'C'
    if col == 'A' and row == 'C':
        return 'A'
    if col == 'A' and row == 'T':
        return 'G'

    if col == 'G' and row == 'A':
        return 'C'
    if col == 'G' and row == 'G':
        return 'G'
    if col == 'G' and row == 'C':
        return 'T'
    if col == 'G' and row == 'T':
        return 'A'

    if col == 'C' and row == 'A':
        return 'A'
    if col == 'C' and row == 'G':
        return 'T'
    if col == 'C' and row == 'C':
        return 'C'
    if col == 'C' and row == 'T':
        return 'G'

    if col == 'T' and row == 'A':
        return 'G'
    if col == 'T' and row == 'G':
        return 'A'
    if col == 'T' and row == 'C':
        return 'G'
    if col == 'T' and row == 'T':
        return 'T'

num = int(input())
dnaCode = list(map(str, input()))
i = 0
while(i != num):
    i += 1
    decode = []
    decode.append(dnaTable(dnaCode[num-i], dnaCode[num-i-1]))
    # print(dnaCode)
    if len(dnaCode) != 1: #dnaCode가 비어있지 않으면
        dnaCode.pop()
        dnaCode.pop()
        dnaCode.append(decode[0])
    else:
        break
print(dnaCode[0])
