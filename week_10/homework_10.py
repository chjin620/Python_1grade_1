print("="*59)
print("■ 202345050 컴시과 1학년 B반 차혜진 11주차 과제 ")
print("■ print("■ if-else, if~elif~else 사용 파일 출력하는 프로그램 ")")
print("-"*59)
print(" >> 생성할 파일명 : testfile.txt ")
print(" >> 생성할 경로명 : C:/Python_Class_B/ ")
print("-"*59)

jul=int(input("몇 줄 데이터를 입력할까요? : "))
print(" ")

fileName=open("C:/Python_Class_B/testfile.txt ","w")

for cnt in range(1,jul+1) :
    hbun=eval(input("학번을 입력하세요 : "))
    irum=input("이름을 입력하세요 : ")
    gubun=eval(input("성별 입력(남->1/여->2) : "))
    if gubun==1:
        gender="남성"
        ki=eval(input("키를 입력하세요 : "))
        if ki >=180:
            gugi="농구"
        else:
            gugi="축구"
    elif gubun==2:
        gender="여성"
        muge=eval(input("체중을 입력하세요 : "))
        if muge <=70:
            gugi="배구"
        else:
            gugi="피구"
    else:
        gender="중성"
        gugi="오류"