class Human:
    head=1
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name}, {self.age}'

    def __len__(self):
        return len(self.name)

    def __abs__(self):
        return abs(self.age)
    def str(self):
        print(f'{self.name}, {self.age}')


#
# hum=Human('Beka',-16)
# print(hum)
# print(abs(hum))
# print(len(hum))

class Student(Human):
    def __str__(self):
        return f'name:{self.name} age:{self.age}'

    def _kill(self,a):
        print(self.name ,'killed',a)

    def str(self):
        print(f'{self.age}, {self.age}')
# stud=Student('Ivan',60)
# print(stud)
# stud._kill(hum.name)

class Human2(Student,Human):
    pass

print('re')
hum2=Human2('Medet',21)
print(hum2)
print('')


