class Car:
    motor=True
    def __init__(self,model,age):
        self.model=model
        self.age=age

    def run(self):
        print(f'{self.model} runnn')



car1=Car('Циррик',1996)
Car.motor=False
car1.run()
print(car1.motor)
