# f'이것은 문자열 {변수 : 0.2f} 입니다'
x = 100 / 3.24
print(f"my number is {x:.3f}")
print()

num1 = 1.23456789
print(f'f-string example1 : {num1:.0f}')
print(f'f-string example2 : {num1:.1f}')
print(f'f-string example3 : {num1:.2f}')
print(f'f-string example4 : {num1:.3f}')
print(f'f-string example5 : {num1:.4f}')
print()


# "이것을 문자열 { : .2f}".format(실수 입력)
a = "format example1 : {:.2f}".format(1.23456789)
print(a)
b = "format example2 : {:.2f} / {:.3f}".format(1.23456789, 3.9876543)
print(b)
c = "format example3 : {0:.2f} / {1:.1f}".format(3.334256, 10.123456)
print(c)
d = "format example4 : {1:.2f} / {0:.1f}".format(3.334256, 10.123456)
print(d)
