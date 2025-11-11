import math


def area(r):
    '''
    Возвращает площадь окружности с радиусом r
        Параметры:
            r (int): радиус окружности
        Возвращаемое значение:
            area (float): площадь окружности
    ''' 
    if(r<0): return 0
    return math.pi * r * r


def perimeter(r):
    '''
    Возвращает длину окружность с радиусом r
        Параметры:
            r (int): радиус окружности
        Возвращаемое значение:
            perimeter (float): длина окружности
    ''' 
    if(r<0): return 0
    return 2 * math.pi * r

