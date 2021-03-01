from time import sleep

class TrafficLight:
#    tl_color = "red"

    def __init__(self, color, tim):
        self.__color = color
        self.tim = tim
      #  print("цвет", color)

    def running(self):
        colors = ['красный', 'желтый', 'зеленый']
        tims = [7, 2, 4]
        for i in range(3):
            color = colors[i]
            tim = tims[i]
            print("цвет", color)
            sleep(int(tim))


my_c_tl = TrafficLight('выкл',0)
my_c_tl.running()