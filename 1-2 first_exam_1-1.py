"""
day 1-2
"""
print("day 1-2")

a = 50
b = 70
sum = a + b

print(sum)

a, b = input().split()
a = int(a)
b = int(b)
sum = a + b
print(sum)

print("결과 확인")

name = "윤경환"
print(name)

age = 21
print(age)

print("나의 이름은 %s이고, %d세입니다."%(name,age))

a, b = input().split()
a = int(a)
b = int(b)
print("합:%d"%(a+b))
print("차:%d"%(a-b))
print("곱:%d"%(a*b))
print("몫:%d"%(a//b))
print("나머지:%d"%(a%b))
