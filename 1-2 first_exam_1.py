"""
day 1-1
"""
print("day 1-1")

print("윤경환")

name = "윤경환"
print(name)

age = 21
print(age)

l = [name,age]
for i in l:
    print(l)

name = input()
print(name)

age = input()
print(age)

name, age = input().split()
print(name)
print(age)

name, age = input("나의 이름은 %s이고, %s세입니다."%(name,age)).split()

age = int(age)







