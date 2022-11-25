class Human:
    head = 1

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def running(self):
        print(f'{self.name} умеет ходить')


hum = Human('Султан', 17)


class Student(Human):

    head = 2
    def __init__(self, name, age, status):
        super().__init__(name, age)
        Human.__init__(self, name, age)
        self.status = status

    def running(self):
        print(f'{self.name} теперь умеет бегать')


student1 = Student('Барсбек', 61, False)
student1.running()
hum.running()
print(student1.status)


class Tefal(Student,Human):
    def __init__(self, name, age, status):
        Student.__init__(self,name, age, status)
# инкапсуляция - скрытие или защита чего либо
# полиморфизм - изменение унаследованных методов и аргументов
# наследование - унаследовать всё у другого класса
