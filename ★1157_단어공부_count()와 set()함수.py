word = input().lower()      # word = mississipi / baaa
words = list(set(word)) # set를 통해서 중복 없애기 ==> word_list = ['m', 'i', 's', 'p'] / ['b', 'a']
cnt = []

for i in words:         # i = m, i, s, p / b, a
    count = word.count(i)  # count()를 통해서 set의 원소의 갯수를 센다.
    cnt.append(count)       # cnt = [4, 4, 1, 1] / [1, 3]

if cnt.count(max(cnt)) >= 2:
    print("?")
else:
    print(words[(cnt.index(max(cnt)))].upper())





'''
word = input()
word = word.lower()
dictionary = {}
for i in word:
    if i not in dictionary:
        dictionary = dict(i = 1)
    else:
        dictionary[i] = dictionary[i] + 1
print(max(dictionary))

==> 시도했던 코드: 틀린 이유는 dictionary에 코드처럼 'i'를 넣으면, for문의 i에
해당하는 값이 들어가지 않고, 진짜로 'i' 값이 들어간다.
그래서 max를 출력하게 되면 i 혼자 출력하게 된다.

'''
