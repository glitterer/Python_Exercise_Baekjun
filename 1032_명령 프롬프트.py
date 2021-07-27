# https://tturbo0824.tistory.com/38\
# 계속 건드리다가 결국 혼자 못 풀었다... 너무 문제를 어렵게 생각했음.

N = int(input())
first_word = list(input())
first_word_len = len(first_word)

for i in range(N - 1):
    other_words = list(input())
    for j in range(first_word_len):
        if first_word[j] != other_words[j]:
            first_word[j] = '?'

print(''.join(first_word))
