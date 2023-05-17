## 동일한 디렉터리에서 새 파일 생성 프로그램
print("="*59)
print("■ 202345050 컴시과 1학년 B반 차혜진 10주차 과제 ")
print("■ 입력받아 파일 열기와 쓰기 프로그램 ")
print("-"*59)
print(" >> 생성할 파일명 : listfile.txt ")
print(" >> 생성할 경로명 : C:/Python_Class_B/ ")
print("-"*59)

jul=int(input("몇 줄 데이터를 입력할까요? : "))
print(" ")

fileName=open("C:/Python_Class_B/listfile.txt ","w")

for cnt in range(1,jul+1) :
    hbun=int(input("학번을 입력하세요 : "))
    irum=input("이름을 입력하세요 : ")
    dept=input("학과를 입력하세요 : ")
    print(" ")
    prt="%02d,%12s,%5s,%3s \r"%(cnt,hbun,irum,dept)
    fileName.write(prt)

fileName.close()

print("\n <<<< <파일 쓰기 완료 >>>>>\n")
print("-"*59)
print(">>C:/Python_Class_B/pathfile.txt 파일의 내용을 확인하세요.")
print("="*59)