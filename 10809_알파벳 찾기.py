word = list(input())
alphabet = "abcdefghijklmnopqrstuvwxyz"
index = []
for i in range(len(list(alphabet))):
    index.append(-1)

pos = 0
#알파벳 위치 찾기
for i in word:  #baek
    cnt = 0
    for j in list(alphabet):
        if j == i and index[cnt] != -1:
            pos += 1
            pass
        elif j == i:
            index[cnt] = pos
            pos += 1
        cnt += 1

for i in range(len(list(alphabet))):
    print(index[i], end = ' ')

    
    '''
    #다른 사람의 풀이
a = input()
for x in range(97, 123):
    print(a.find(chr(x)), end=" ")
    '''
