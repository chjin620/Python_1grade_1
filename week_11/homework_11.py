print("="*59)
print("■ 202345050 컴시과 1학년 B반 차혜진 11주차 과제 ")
print("■ 입력받아 파일 열기와 쓰기 프로그램 ")
print("-"*59)
print(" >> 생성할 파일명 : testfile.txt ")
print(" >> 생성할 경로명 : C:/Python_Class_B/ ")
print("-"*59)
jul=int(input("몇 줄 데이터를 입력할까요? : "))
print(" ")
fileName=open("C:/Python_Class_B/testfile.txt ","w")
for cnt in range(1,jul+1) :
    hbun=eval(input("학번을 입력하세요     : "))
    irum=input("이름을 입력하세요    : ")
    gubun=eval(input("성별 입력(남->1/여->2) :"))
    if gubun==1:
        gender="남성"
        ki=eval(input("키를 입력하세요    : "))
        if ki >=180:
            gugi="농구"
        else:
            gugi="축구"
    elif gubun==2:
        gender="여성"
        muge=eval(input("체중을 입력하세요    : "))
        if muge <=70:
            gugi="배구"
        else:
            gugi="피구"
    else:
        gender="중성"
        gugi="오류"

    score=eval(input("점수를 입력하세요    : "))
    if score>100 or score<0:
        jumsu="Er"
    else:
        if score>=95:
            jumsu="A+"
        elif score>=90:
            jumsu="A"
        elif score>=85:
            jumsu="B+"
        elif score>=80:
            jumsu="B"
        elif score>=75:
            jumsu="C+"
        elif score>=70:
            jumsu="C"
        elif score>=65:
            jumsu="D+"
        elif score>=60:
            jumsu="D"
        else :
            jumsu="F"


    print(" ")
    ppp="%02d, %12s, %5s, %3s,%s,%s \n"%(cnt, hbun,irum,gugi,score,jumsu)
    fileName.write(ppp)
fileName.close()
print("\n <<<< <파일 쓰기 완료 >>>>>\n")
print("-"*59)
print(">>C:/Python_Class_B/testfile.txt 파일의 내용을 확인하세요.")
print("="*59)