# Реализуйте класс Car (машина).

class Car:

    def __init__(self, speed, color, name, is_police: False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} поехала')

    def stop(self):
        print(f'{self.name} остановилась')

    def turn(self, direction):
        if self.speed > 40:
            lim_spd = self.speed - 40
            self.speed -= lim_spd
        print(f'{self.name} повернул на {direction}')

    def show_speed(self):
        print(f'Скорость {self.speed}')
        return self.speed


class TownCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print('Привышена скорость в 60')
        return self.speed


class SportCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print('Привышена скорость в 40')
        return self.speed


class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        self.is_police = True


town = TownCar(100, 'Белая', 'Лада', False)
town.go()
town.show_speed()
town.turn('Право')
town.stop()

sport = SportCar(200, 'Красная', 'Феррари', False)
sport.go()
sport.show_speed()
sport.turn('Лево')
sport.stop()

work = WorkCar(50, 'Серый', 'Фиат', False)
work.go()
work.show_speed()
work.turn('Право')
work.stop()

police = PoliceCar(100, 'Синий', 'Форд', True)
police.go()
police.show_speed()
police.turn('Лево')
police.stop()
