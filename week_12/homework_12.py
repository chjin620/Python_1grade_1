print("="*55)
print("■ 202345050 컴시과 1학년 B반 차혜진 12주차 실습")
print("■ 입력받은 수의 구구단을 출력하는 프로그램")
print(" >> 생성할 파일명 : calfile.txt ")
print(" >> 생성할 경로명 : C:/Python_Class_B/ ")
print("-"*55)

fileName=open("C:/Python_Class_B/calfile.txt ","w")

out_cnt=0
while 1 :

    choiceValue=input(">> 프로그램을 실행하시겠습니까? (Y/N) : ")
    print("-"*55)

    if choiceValue=='Y' or choiceValue=='y' :
        out_cnt +=1

        print(">> 구구단은 2~9 숫자만 입력하세요.")
        print("-"*55)

        while 1 :
            dan=int(input(">> 몇의 단을 출력할까요? : "))
            print("-"*55)

            if dan<2 or dan>9 :
                print(">> 유효숫자 범위 오류!!!")
                print(">> 숫자를 다시 입력하세요...")
                print("-"*55)
                continue

            else:
                print(">> %2d의 구구단 출력 << "%dan)
                fileName.write(">> %2d 의 구구단\n"%dan)

                for cnt in range(1, 10):
                    print("%5d x %2d = %2d"%(dan, cnt, dan*cnt))
                    fileName.write(" %5d x %2d = %2d\n"%(dan, cnt, dan*cnt))
                if cnt==9:
                    print('-'*55)
                    print(">> %2d의 단을 출력하였습니다."%dan)
                    print("-"*55)
                    break
    elif choiceValue=='N' or choiceValue=='n':
        break
    else:
        print(">> 알파벳을 잘못 입력하였습니다.")
        print('-'*55)
        continue
fileName.close()

if out_cnt!=0:
    print(">> 총 %d 회 반복 실행 후 프로그램을 종료합니다."%out_cnt)
    print('='*55)
    print("<<<< 파일 쓰기 완료 >>>>>")
    print('-'*55)
    print(">> C/Python_ex/calfile.txt 파일 내용을 확인하세요..")
else:
    print(">> 프로그램 실행 하지 않고 프로그램을 종료합니다.")