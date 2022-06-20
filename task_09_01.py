# Создать класс TrafficLight (светофор).

from time import sleep


class TrafficLight:
    def __init__(self, red_time, yell_time, green_time):
        self.__color = ['Красный', 'Желтый', 'Зеленый']
        self.clr = None
        self.gen2 = [0, 1, 2, 1]
        self.t1 = red_time
        self.t2 = yell_time
        self.t3 = green_time

    def state(self):
        return self.__color[self.clr]

    def running(self):
        try:
            while True:
                for i in self.gen2:
                    print(self.__color[i])
                    if self.__color[i] == 'Красный':
                        sleep(self.t1)
                        self.clr = i
                    elif self.__color[i] == 'Желтый':
                        sleep(self.t2)
                        self.clr = i
                    else:
                        sleep(self.t3)
                        self.clr = i
        except KeyboardInterrupt:
            print('Вы прервали программу')


t = TrafficLight(7, 2, 2)
t.running()