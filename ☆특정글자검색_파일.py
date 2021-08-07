def count_word(text, word):
    text_save = open("Q2_content.txt", "w", encoding="UTF8")   # 파일을 쓸 수 있도록 연다
    text_save.write(text)   # 파일에 text를 쓴다.
    text_save.close()   # 파일을 닫는다.

    file_read = open("Q2_content.txt", "r", encoding="UTF8")  # 파일을 읽을 수 있도록 연다.
    data = file_read.read()  # 파일의 내용을 string으로 변환한다.
    frequency = data.count(word)  # word에 해당하는 글자가 전체 글에서 몇개 들어있는지
    print(frequency)


# 입력
word = input("Enter the word to find: ")  #찾고자 하는 글자 검색

a = """안녕하세요.
반갑습니다. 파이썬 공부는 정말 재밌습니다.
"""

count_word(a, word)
