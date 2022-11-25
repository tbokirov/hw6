class Hero:
    def __init__(self, power=0, speed=0, stamina=0, fly=0):
        self.__power = power
        self.__speed = speed
        self.__stamina = stamina
        self.__fly = fly
    def setpwr(self, power):
        self.__power = power
    def getpwr(self):
        return self.__power
    def setspd(self, speed):
        self.__speed = speed
    def getspd(self):
        return self.__speed
    def setstmn(self, stamina):
        self.__stamina = stamina
    def getstmn(self):
        return self.__stamina
    def setfly(self, fly):
        self.__fly = fly
    def getfly(self):
        return self.__fly

hr = Hero()
hr.setpwr(60)
hr.setspd(90)
hr.setstmn(180)
hr.setfly(30)
print(f'Сила-{hr.getpwr()} \nСкорость-{hr.getspd()} '
      f'\nВыносливость-{hr.getstmn()} \nСпособность летать-{hr.getfly()}')