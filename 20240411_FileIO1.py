#1번 다음 보기를 입력과 관련된 함수와 출력과 관련된 함수로 분류하세요.
#입력 :input(), read(), readline(), readlines()
#출력 : print(), write(), writeline()

#2번 파일 처리단계의 순서 나열한 것이 맞는 것을 고르세요.  답 : a(파일열기)-c(파일읽기)-b(파일쓰기)-d(파일닫기)

#3번 파일의 열기 모드에 대한 설명으로 거리가 먼 것을 고르세요. 답 : 4 텍스트 모드가 아니라 텍스트 파일 모드이다.

#4번
inFp = open("C:/Temp/data1.txt", "r")

inStr = inFp.readline()
print(inStr, end = "")

inFp.close()

#6번
inFp = open("C:/Windows/win.ini", "r")
outFp = open("C:/Temp/data3.txt", "r")

inList = inFp.readlines()
for inStr in inList :
    outFp.write(inStr)

inFp.close()
outFp.close()
