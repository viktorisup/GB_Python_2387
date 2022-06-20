# Написать декоратор для логирования(вывод в консоль) типов позиционных аргументов функции:

def type_logger(func):
    def tmp(*args, **kwargs):
        rez = func(*args, **kwargs)
        name = func.__name__
        print(f'Call for: {name}')
        for arg in args:
            print(f'{arg} : {type(arg)}')
        for kwarg in kwargs:
            value = kwargs[kwarg]
            print(f'{kwarg} = {value} : {type(value)}')
        print(f'Rezult: {rez} type: {type(rez)}')
        return rez
    return tmp


@ type_logger
def calc_cube(x):
    return x ** 3

@type_logger
def render_input(*args, **kwargs):
    return 1

calc_cube(5)
render_input(1, 3, a=2, b=True, c="q")