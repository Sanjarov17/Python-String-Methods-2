templete = 'salom mening ismim {name} va yoshim {age}.'

name = input()
age = int(input())

print(templete.format(name=name, age=age))