### assignment1 ###
#5번
ss = 'Python'
for i in range(0,6) :
  print(ss[i] +'$', end = '')
  
#11번
import re
문자열 = '파이썬###CookBook$$$@@@열공중1234'
cleaned_text = re.sub(r'[^가-힣a-zA-Z]', '', 문자열)
print(cleaned_text)

#9번
inStr, outStr = "Python", ""
strLen = len(inStr)
for i in range(0, strLen) :
  outStr +=inStr[strLen -(i+1)]
print("내용을 거꾸로 출력 --> %s" % outStr)



### assignment2 ###
#3번
def plus(v1,v2,v3):
  result = 0
  result = v1 + v2 + v3
  return result
hap = plus(100, 200, 300)
print(hap)

#4번 f1()=100, f2()=10
def f1():
  print(var)
def f2():
  var=10
  print(var)
var=100
f1()
f2()

#11번
def addNumber(num):
  if num == 1:
    return 1
  else:
    return num + addNumber(num - 1)
print(addNumber(100))

#8번
def myFunc(p1=1, p2=2, p3=3):
  ret = p1+p2+p3
  return ret
print("매개변수 없이 호출 ==>", myFunc())
print("매개변수가 1개로 호출 ==>", myFunc(1))
print("매개변수가 2개로 호출 ==>", myFunc(1,2))
print("매개변수가 3개로 호출 ==>", myFunc(1,2,3))

