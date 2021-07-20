num = 255
print(int('111',2))
print(int('222',3))
print(int('333',4))
print(int('444',5))
print(int('555',6))
print(int('FFF',16))

print('{:#b}'.format(num)[2:])
print('{:#o}'.format(num)[2:])
print('{:#x}'.format(num)[2:])

print(format(num, 'b')) #2진수 변환
print(format(num, 'o')) #8진수 변환
print(format(num, 'x')) #16진수 변환

print(bin(num)[2:])
print(oct(num)[2:])
print(hex(num)[2:])
