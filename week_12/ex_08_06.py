## for문으로 1부터 100까지 한 행에 10개씩 출력하는 프로그램  ##
print("=" * 55)
print("■ 1부터 100까지 한 행에 10개씩 출력하는 프로그램")
print("-" * 55)

number = int(input(">> 어디까지 출력할까요? : "))
print("-" * 55)

for cnt in range(1, number+1, 1) :

    print("%5d" % cnt, end='')

    if cnt % 10 == 0 :
        print("")

print("-" * 55)
print(">> 총 %d 회를 수행하였습니다." % cnt)

print("-" * 55)
print("프로그램을 종료합니다.")
print("=" * 55)