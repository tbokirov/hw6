class Person:
    def __init__(self, name):
        self.name = name


p = Person('Ivan')
p.name = 'Beka'
print(p.name)


class Person1:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        print('это геттер')
        return self._name
    def set_name(self,value):
        print('это сеттер set-name')
        self._name = value
    name = property(fget=get_name,fset=set_name)

po=Person1('Ivan')
po.name= ''
print(po.__dict__)
