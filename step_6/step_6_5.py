from random import randint
class Stationery:

    def __init__(self, title):
        self.title = title

    def draw (self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Запуск отрисовки ручки')
class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Запуск отрисовки карандаша')

class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Запуск отрисовки маркера')

title = randint(0, 3)
print(title)
if title == 0:
    print('прочее')
    my_c_stationery = Stationery(title)
    my_c_stationery.draw()
if title == 1:
    print('ручка')
    my_c_pen = Pen(title)
    my_c_pen.draw()

if title == 2:
    print('карандаш')
    my_c_pencil = Pencil(title)
    my_c_pencil.draw()
if title == 3:
    print('маркер')
    my_c_handle = Handle(title)
    my_c_handle.draw()
