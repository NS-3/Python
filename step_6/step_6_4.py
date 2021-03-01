from random import randint


class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go (self):
        print('едет')
    def stop (self):
        print('остановилась')
    def turn (self):
        r = randint(0, 1)
        if r == 1:
            print('повернула направо')
        else: print('повернула налево')

    def show_speed(self):
        speed = randint(0, 100)
        print(f'передвигается со скоростью {speed} км/ч')
        return (speed)



class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        speed = randint(0, 100)
        print(f'городская машина передвигается со скоростью {speed} км/ч')
        if speed > 60:
            print('городская машина превысила допустимую скорость 60 км/ч111')

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def sport(self):
        print('спортивная')
class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        speed = randint(0, 100)
        print(f'рабочая машина передвигается со скоростью {speed} км/ч')
        if speed > 40:
            print('рабочая машина превысила допустимую скорость 40 км/ч111')
class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def polic(self):
        print('это полиция')
speed = randint(0, 100)
#print('speed', speed)
colors = ['красный', 'оливковый', 'зеленый', 'желтый', 'белый', 'черный']
i = randint(0, 5)
color = colors[i]
#print('цвет:', color)
#color = input('введите цвет: ')
names = ['Audi', 'BMW', 'Ford', 'Honda', 'Hyundai', 'Kia', 'Lada (ВАЗ) ', 'Mazda', 'Mercedes-Benz', 'Mitsubishi', 'Nissan', 'Renault', 'Skoda', 'Toyota', 'Volkswagen']
i = randint(0, 14)
name = names[i]

print(f'машина цвета {color}, марки {name}, выехала со скоростью {speed}км/ч')


p = randint(0, 3)
if p == 1:
    is_police = True
    my_c_policeCar = PoliceCar(speed, color, name, is_police)
    my_c_policeCar.polic()


else:
    is_police = False
    print(f'это не полиция {p}')
if p == 0:
    my_c_sportCar = SportCar(speed, color, name, is_police)
    my_c_sportCar.sport()

my_c_car = Car(speed, color, name, is_police)
my_c_car.show_speed()
if speed == 0:
    my_c_car.stop()
else:
 #   my_c_car_pol.go()
    my_c_car.go()
    t = randint(0, 1)
#    print('t', t)
    if t == 1:
        my_c_car.turn()
    else: print('прямо')

if p == 2:
    my_c_townCar = TownCar(speed, color, name, is_police)
    my_c_townCar.show_speed()
if p == 3:
    my_c_workCar = WorkCar(speed, color, name, is_police)
    my_c_workCar.show_speed()