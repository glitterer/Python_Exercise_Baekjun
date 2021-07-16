repeat = int(input())
for i in range(0, repeat):
    str = input()
    cnt_vowel = 0
    cnt_const = 0
    for j in str:
        if j == 'a' or j == 'e' or j == 'i' or j == 'o' or j == 'u' or j == 'A' or j == 'E' or j == 'I' or j == 'O' or j == 'U':
            cnt_vowel = cnt_vowel + 1
        elif j == ' ':
            continue
        else:
            cnt_const = cnt_const + 1
    print(cnt_const, cnt_vowel, sep = ' ')
