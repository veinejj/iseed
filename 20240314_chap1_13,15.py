###13번문제###  답 : 전부, 10진수로 입력된 값을 2,8,16진수로 읽으려고 하기 때문이다.
str('1002', 2)

int('1008', 8)

int('AAFG', 16)

###15번문제###
num = 12345678
hex_num = hex(num)
oct_num = oct(num)
bin_num = bin(num)

print("10진수 ==> ", num)
print("16진수 ==> ", hex_num)
print("8진수 ==> ", oct_num)
print("2진수 ==> ", bin_num)
