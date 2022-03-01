### 반복문(for) Programmer : 홍길동 ###
for i in range(0, 10, 2) :
    print(i, end= "  ")
print()
for _ in range(5) :
    print("경영정보학과")

### 1~100까지 합을 계산 ###
sum = 0
for i in range(2,101, 2) :
    sum += i
print("합은 %d" % sum)

### ??? ######
su = int(input("수를 입력="))
for i in range(2, 10, 1) :
    print("%d * %d = %d" %(su, i, su*i))

