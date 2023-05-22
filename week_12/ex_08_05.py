## 딕셔너리를 사용하여 특정 숫자가 입력되기 전까지 무한 반복을 수행하는 프로그램 ##
print("="*55)
print("■ 딕셔너리를 사용한 무한반복 프로그램")
print("-"*55)

## """를 사용하면 열 바꿔쓰기 가능
number={1: '컬링'
        2: '피겨스케이팅'
        3: '알파인스키'
        4: '봅슬레이'
        5: '쇼트트랙'
        6: '그냥 종료'}

choiceValue=0

while choiceValue !=6 :
    print(">> 동계올림픽 경기종목 선택\n")
    print(number)
    print("-"*55)
    choiceValue=int(input(">> 선호종목 선택(1~6) : "))
    print("-"*55)

    if choiceValue==6 :
        pass
    elif choiceValue>6 :
        print(">> 잘못 선택하였으므로 다시 선택하세요.")
    ##기존 예제에 7이상의 숫자를 넣었을 때 잘못선택했음을 알려주는 문장 추가
    else :
        print(">> 선택한 종목 : [ ", end='')
        print(number.get(choiceValue)+"]")
        print(">> 계속해서 다른 종목을 선택할수 있습니다.")
        print("-"*55)

print(">> 선택한 종목 : [ ", end='')
print(number.get(choiceValue)+"]")
print(">> 숫자 [%d]이 입력되었으므로 프로그램을 종료합니다."%choiceValue)
print("="*55)