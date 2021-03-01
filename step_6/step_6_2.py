from random import randint


class Road:
#    tl_color = "red"

    def __init__(self, length, width):
        self._length = length
        self._width = width


    def val(self):
        h = randint(1, 10)
        mass = randint(25, 30)
        massa = Road._length * Road._width * mass * h / 1000
        print(f'масса асфальта для дороги шириной {Road._width}м, длиной {Road._length}м, высотой слоя {h}см при массе слоя 1см {mass}кг составляет {massa}т')
        return (massa)


Road._length = randint(1, 1000)
Road._width = randint(1, 100)



my_c_road = Road(Road._length, Road._width)
my_c_road.val()


