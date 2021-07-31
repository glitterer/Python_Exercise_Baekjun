word = list(input())
print(word)
alphabet = "abcdefghijklmnopqrstuvwxyz"
index = []
for i in range(len(list(alphabet))):
    index.append(0)

#알파벳에 따라서 인덱스 값 할당
for i in word:  #baek
    cnt = 0
    for j in list(alphabet):
        if i == j:
            index[cnt] += 1
        cnt += 1

for i in range(len(list(alphabet))):
    print(index[i], end = ' ')
